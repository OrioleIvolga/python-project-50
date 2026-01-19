from .parsers import parse_file


def _format_value(value):
    """Преобразует Python-значение в строку в JSON-стиле."""
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    else:
        return str(value)


def _build_line(key, value, status):
    """Формирует одну строку diff в зависимости от статуса."""
    formatted_value = _format_value(value)
    if status == 'unchanged':
        return f"    {key}: {formatted_value}"
    elif status == 'removed':
        return f"  - {key}: {formatted_value}"
    elif status == 'added':
        return f"  + {key}: {formatted_value}"
    elif status == 'changed':
        # Этот случай обрабатывается двумя вызовами: сначала removed, потом added
        raise ValueError("Use separate calls for 'removed' and 'added' in 'changed' case")


def generate_diff(file1_path, file2_path, format_name='stylish'):
    """
    Генерирует diff между двумя плоскими JSON/YAML-файлами.
    Возвращает строку в формате 'stylish'.
    """
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    lines = []

    for key in all_keys:
        in1 = key in data1
        in2 = key in data2

        if in1 and in2:
            if data1[key] == data2[key]:
                lines.append(_build_line(key, data1[key], 'unchanged'))
            else:
                # Сначала значение из первого файла (удалено), потом из второго (добавлено)
                lines.append(_build_line(key, data1[key], 'removed'))
                lines.append(_build_line(key, data2[key], 'added'))
        elif in1:
            lines.append(_build_line(key, data1[key], 'removed'))
        else:  # in2 only
            lines.append(_build_line(key, data2[key], 'added'))

    result = "{\n" + "\n".join(lines) + "\n}"
    return result
