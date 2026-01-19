

def _format_plain_value(value):
    """Форматирует значение для plain-вывода."""
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return repr(value)  # добавит кавычки: 'blah blah'
    else:
        # числа, списки и т.д. — преобразуем в строку без кавычек
        return str(value)


def _build_plain(diff_tree, parent_path=""):
    """Рекурсивно строит строки plain-формата."""
    lines = []

    for node in diff_tree:
        key = node["key"]
        current_path = f"{parent_path}.{key}" if parent_path else key

        match node["type"]:
            case "nested":
                nested_lines = _build_plain(node["children"], current_path)
                lines.extend(nested_lines)
            case "added":
                value_str = _format_plain_value(node["value"])
                lines.append(f"Property '{current_path}' was added with value: {value_str}")
            case "removed":
                lines.append(f"Property '{current_path}' was removed")
            case "changed":
                old_val = _format_plain_value(node["value"]["old"])
                new_val = _format_plain_value(node["value"]["new"])
                lines.append(f"Property '{current_path}' was updated. From {old_val} to {new_val}")
            # unchanged — не выводим

    return lines


def format_plain(diff_tree):
    """Основная функция форматера 'plain'."""
    lines = _build_plain(diff_tree)
    return "\n".join(lines)
