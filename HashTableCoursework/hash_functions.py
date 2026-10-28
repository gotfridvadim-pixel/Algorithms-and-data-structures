def additive_hash(key):
    """Вычисляет аддитивный хеш строкового ключа.

    Хеш равен сумме кодов всех символов строки.

    Args:
        key: Строковый ключ.

    Returns:
        Целочисленное значение хеша.

    Raises:
        TypeError: Если ключ не является строкой.
    """

    if isinstance(key, str):
        return sum(ord(char) for char in key)

    raise TypeError(f"Неподдерживаемый тип ключа: {type(key).__name__}")


def polynomial_hash(key):
    """Вычисляет полиномиальный хеш строкового ключа.

    Для строки каждый следующий символ добавляется к накопленному хешу
    с использованием основания 31.

    Args:
        key: Строковый ключ.

    Returns:
        Целочисленное значение хеша.

    Raises:
        TypeError: Если ключ не является строкой.
    """

    if isinstance(key, str):
        h = 0
        for char in key:
            h = h * 31 + ord(char)
        return h

    raise TypeError(f"Неподдерживаемый тип ключа: {type(key).__name__}")
