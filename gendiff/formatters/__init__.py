from .plain import format_plain
from .stylish import format_stylish

FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
}
