from .diff_builder import build_diff
from .formatters.stylish import format_stylish
from .parsers import parse_file


def generate_diff(file1_path, file2_path, format_name='stylish'):
    """
    Генерирует diff между двумя JSON/YAML-файлами (плоскими или вложенными).
    Поддерживаемый формат вывода: 'stylish'.
    """
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)

    diff_tree = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff_tree)
    else:
        raise ValueError(f"Unsupported format: {format_name}")
