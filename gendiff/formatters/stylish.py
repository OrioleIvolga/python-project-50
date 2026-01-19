from ..utils import format_value


def format_stylish(diff_tree: list, depth=0) -> str:
    indent_size = 4
    current_indent = " " * (depth * indent_size)
    lines = ["{"]

    for node in diff_tree:
        key = node["key"]
        match node["type"]:
            case "nested":
                nested_lines = format_stylish(node["children"], depth + 1)
                lines.append(f"{current_indent}    {key}: {nested_lines}")
            case "unchanged":
                value = format_value(node["value"])
                lines.append(f"{current_indent}    {key}: {value}")
            case "added":
                value = format_value(node["value"])
                lines.append(f"{current_indent}  + {key}: {value}")
            case "removed":
                value = format_value(node["value"])
                lines.append(f"{current_indent}  - {key}: {value}")
            case "changed":
                old_val = format_value(node["value"]["old"])
                new_val = format_value(node["value"]["new"])
                lines.append(f"{current_indent}  - {key}: {old_val}")
                lines.append(f"{current_indent}  + {key}: {new_val}")

    lines.append(current_indent + "}")
    return "\n".join(lines)
