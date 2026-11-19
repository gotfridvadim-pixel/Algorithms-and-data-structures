"use strict";

const form = document.getElementById("controls");
const fields = document.getElementById("fields");
const result = document.getElementById("result");
const calculation = document.getElementById("calculation");
const retry = document.getElementById("retry");
const bucketList = document.getElementById("buckets");
const submit = document.getElementById("submit");
const captions = { put: "Добавить в таблицу", find: "Найти ключ", delete: "Удалить ключ" };
let capacity = 0;

function element(tag, className, text) {
  const node = document.createElement(tag);
  node.className = className;
  node.textContent = text;
  return node;
}

function drawTable(state) {
  const rows = document.createDocumentFragment();
  let count = 0;
  let longest = 0;
  state.buckets.forEach((pairs, index) => {
    const active = index === state.index;
    const row = element("li", active ? "row active" : "row", "");
    row.setAttribute("aria-label", "Корзина " + index);
    row.append(element("span", "index", String(index).padStart(2, "0")));
    const chain = element("div", "chain", "");
    pairs.forEach(([key, value], position) => {
      if (position > 0) {
        const arrow = element("span", "link", "→");
        arrow.setAttribute("aria-hidden", "true");
        chain.append(arrow);
      }
      const pair = element("span", active && key === state.key ? "node hit" : "node", "");
      pair.append(element("b", "", key), element("small", "", value));
      chain.append(pair);
    });
    if (!pairs.length) chain.append(element("span", "empty", "пусто"));
    row.append(chain);
    rows.append(row);
    count += pairs.length;
    longest = Math.max(longest, pairs.length);
  });
  bucketList.replaceChildren(rows);
  capacity = state.buckets.length;
  document.getElementById("capacity").textContent = "Корзин · " + capacity;
  document.getElementById("size").textContent = count;
  document.getElementById("load").textContent = new Intl.NumberFormat("ru", {
    style: "percent", maximumFractionDigits: 1
  }).format(count / capacity);
  document.getElementById("longest").textContent = longest;
  const activeRow = bucketList.querySelector(".active");
  if (activeRow && bucketList.scrollHeight > bucketList.clientHeight) {
    bucketList.scrollTop += activeRow.getBoundingClientRect().top - bucketList.getBoundingClientRect().top;
  }
}

async function api(path, options) {
  let response;
  try {
    response = await fetch(path, options);
  } catch {
    throw new Error("Нет связи с Python-сервером. Проверьте, что он запущен.");
  }
  if (!response.headers.get("content-type")?.includes("application/json")) {
    throw new Error("Откройте страницу по адресу, который вывел web_server.py.");
  }
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || "Не удалось получить данные таблицы.");
  return data;
}

async function loadTable() {
  retry.hidden = true;
  fields.disabled = true;
  calculation.textContent = "";
  try {
    drawTable(await api("/api/table"));
    result.textContent = "Попробуйте найти «кот» или добавить свой ключ.";
    fields.disabled = false;
  } catch (error) {
    result.textContent = error.message;
    retry.hidden = false;
  }
}

form.addEventListener("change", (event) => {
  if (event.target.name !== "action") return;
  const action = form.elements.action.value;
  document.getElementById("value-field").hidden = action !== "put";
  form.elements.value.disabled = action !== "put";
  submit.textContent = captions[action];
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (fields.disabled) return;
  const data = Object.fromEntries(new FormData(form));
  const previousCapacity = capacity;
  fields.disabled = true;
  calculation.textContent = "";
  try {
    const state = await api("/api/operation", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
    drawTable(state);
    result.textContent = state.message + (capacity > previousCapacity
      ? " Число корзин выросло с " + previousCapacity + " до " + capacity + "." : "");
    calculation.textContent = state.hash + " mod " + capacity + " = " + state.index;
  } catch (error) {
    result.textContent = error.message;
  } finally {
    fields.disabled = false;
  }
});

retry.addEventListener("click", loadTable);
document.querySelector(".bar a").addEventListener("click", () => {
  document.getElementById("principle").open = true;
});
loadTable();
