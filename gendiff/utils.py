def format_value(value, depth=0):
    """
    Преобразует значение в строку для stylish-формата.
    Рекурсивно обрабатывает словари.
    """
    if isinstance(value, dict):
        if not value:
            return "{}"
        indent = "    " * (depth + 1)
        lines = ["{"]
        for key in sorted(value.keys()):
            val_str = format_value(value[key], depth + 1)
            lines.append(f"{indent}{key}: {val_str}")
        closing_indent = "    " * depth
        lines.append(f"{closing_indent}}}")
        return "\n".join(lines)

    # Обработка специальных значений
    if value is None:
        return ''  # ← ВАЖНО: не 'null', а пустая строка!
    if isinstance(value, bool):
        return str(value).lower()  # true / false
    return str(value)
