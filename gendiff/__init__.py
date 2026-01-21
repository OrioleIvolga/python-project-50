from .diff_builder import build_diff
from .formatters import FORMATTERS
from .parsers import parse_file


def generate_diff(file1_path, file2_path, format_name='stylish'):
    if format_name not in FORMATTERS:
        raise ValueError(
            f"Unsupported format: {format_name}. "
            f"Supported: {list(FORMATTERS.keys())}"
            )

    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)

    diff_tree = build_diff(data1, data2)
    formatter = FORMATTERS[format_name]
    return formatter(diff_tree)

# gendiff/__init__.py
