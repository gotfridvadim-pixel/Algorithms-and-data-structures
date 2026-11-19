"""Local web interface for the coursework. Run alongside hash_table.py."""

import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from urllib.parse import urlsplit

from hash_functions import additive_hash
from hash_table import HashTable


WEB = Path(__file__).resolve().parent / "web"
ASSETS = {
    "/": ("index.html", "text/html"),
    "/style.css": ("style.css", "text/css"),
    "/app.js": ("app.js", "text/javascript"),
}


def example_table():
    table = HashTable(capacity=4, hash_func=additive_hash)
    for key, value in [("лес", "глушь"), ("кот", "животное"), ("ток", "электричество")]:
        table.insert(key, value)
    return table


def field(data, name, limit):
    value = data.get(name)
    if not isinstance(value, str) or not 1 <= len(value.strip()) <= limit:
        label = "ключ" if name == "key" else "значение"
        raise ValueError(f"Введите {label} длиной от 1 до {limit} символов.")
    return value.strip()


def apply_operation(table, data):
    action = data.get("action")
    key = field(data, "key", 48)
    if action == "put":
        value = field(data, "value", 96)
        exists = key in table
        table[key] = value
        message = f"Значение для «{key}» обновлено." if exists else f"Ключ «{key}» добавлен."
    elif action == "find":
        value = table.search(key)
        message = f"Найдено значение «{value}»." if value is not None else f"Ключ «{key}» отсутствует."
    elif action == "delete":
        exists = key in table
        table.delete(key)
        message = f"Ключ «{key}» удалён." if exists else f"Ключ «{key}» отсутствует."
    else:
        raise ValueError("Выберите добавление, поиск или удаление.")
    buckets = table.get_view()
    hash_value = additive_hash(key)
    return dict(buckets=buckets, key=key, hash=hash_value, index=hash_value % len(buckets), message=message)


class Handler(BaseHTTPRequestHandler):
    def respond(self, status, content, mime):
        self.send_response(status)
        self.send_header("Content-Type", mime + "; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(content)

    def json_response(self, status, payload):
        self.respond(status, json.dumps(payload, ensure_ascii=True).encode(), "application/json")

    def do_GET(self):
        path = urlsplit(self.path).path
        if path == "/api/table":
            with self.server.table_lock:
                buckets = self.server.table.get_view()
            return self.json_response(200, {"buckets": buckets})
        if path in ASSETS:
            name, mime = ASSETS[path]
            return self.respond(200, (WEB / name).read_bytes(), mime)
        self.send_error(HTTPStatus.NOT_FOUND)

    def do_POST(self):
        if urlsplit(self.path).path != "/api/operation":
            return self.send_error(HTTPStatus.NOT_FOUND)
        if self.headers.get_content_type() != "application/json":
            return self.json_response(415, {"error": "Ожидается JSON."})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 8192:
                raise ValueError("Некорректный размер запроса.")
            data = json.loads(self.rfile.read(length).decode("utf-8"))
            if not isinstance(data, dict):
                raise ValueError("Ожидается объект JSON.")
            with self.server.table_lock:
                result = apply_operation(self.server.table, data)
        except (ValueError, RecursionError) as error:
            return self.json_response(400, {"error": str(error)})
        self.json_response(200, result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000)
    port = parser.parse_args().port
    with ThreadingHTTPServer(("127.0.0.1", port), Handler) as server:
        server.table = example_table()
        server.table_lock = Lock()
        print(f"http://127.0.0.1:{server.server_port}/", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
