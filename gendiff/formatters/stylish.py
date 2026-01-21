# gendiff/formatters/stylish.py
from ..utils import format_value


def format_stylish(diff_tree, depth=0):
    """
    Formats the diff tree into 'stylish' plain-text representation.

    Args:
        diff_tree: List of diff nodes.
         Each is a dict with 'key', 'type', and 'value'.
        depth: Current nesting level for indentation

    Returns:
        Formatted string representing the diff.
    """
    current_indent = "    " * depth
    lines = ["{"]

    for node in diff_tree:
        key = node["key"]
        node_type = node["type"]

        if node_type == "nested":
            nested_result = format_stylish(node["children"], depth + 1)
            lines.append(f"{current_indent}    {key}: {nested_result}")
        elif node_type == "unchanged":
            value_str = format_value(node["value"], depth + 1)
            lines.append(f"{current_indent}    {key}: {value_str}")
        elif node_type == "added":
            value_str = format_value(node["value"], depth + 1)
            lines.append(f"{current_indent}  + {key}: {value_str}")
        elif node_type == "removed":
            value_str = format_value(node["value"], depth + 1)
            lines.append(f"{current_indent}  - {key}: {value_str}")
        elif node_type == "changed":
            old_str = format_value(node["value"]["old"], depth + 1)
            new_str = format_value(node["value"]["new"], depth + 1)
            lines.append(f"{current_indent}  - {key}: {old_str}")
            lines.append(f"{current_indent}  + {key}: {new_str}")

    lines.append(current_indent + "}")
    return "\n".join(lines)
