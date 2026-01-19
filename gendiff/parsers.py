import json

import yaml


def parse_file(filepath: str) -> dict:
    """
    Читает файл и парсит его содержимое в зависимости от расширения.
    Поддерживаемые форматы: .json, .yml, .yaml
    """
    if filepath.endswith('.json'):
        with open(filepath, 'r') as f:
            return json.load(f)
    elif filepath.endswith(('.yml', '.yaml')):
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
            return data if data is not None else {}
    else:
        raise ValueError(f"Unsupported file format: {filepath}. "
                         "Supported: .json, .yml, .yaml")
