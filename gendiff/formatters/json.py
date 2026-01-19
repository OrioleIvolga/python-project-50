import json


def _convert_value(value):
    """Преобразует значение для сериализации в JSON."""
    if isinstance(value, dict):
        # Рекурсивно обрабатываем словари (например, в changed)
        return {k: _convert_value(v) for k, v in value.items()}
    elif isinstance(value, bool):
        return value  # JSON поддерживает true/false
    elif value is None:
        return None   # → null
    else:
        return value


def _format_node(node):
    """Преобразует узел дерева в JSON-совместимый словарь."""
    result = {"key": node["key"], "type": node["type"]}

    if node["type"] == "nested":
        result["children"] = [_format_node(child) for child in node["children"]]
    elif node["type"] == "changed":
        result["value"] = {
            "old": _convert_value(node["value"]["old"]),
            "new": _convert_value(node["value"]["new"])
        }
    else:
        # added, removed, unchanged
        result["value"] = _convert_value(node["value"])

    return result


def format_json(diff_tree):
    """Сериализует diff-дерево в JSON-строку."""
    json_ready = [_format_node(node) for node in diff_tree]
    return json.dumps(json_ready, indent=4)
