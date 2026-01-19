def format_value(value):
    """Преобразует Python-значение в строку в JSON-стиле."""
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    else:
        return str(value)
