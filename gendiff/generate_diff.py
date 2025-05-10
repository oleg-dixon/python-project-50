from gendiff.diff_tree import build_diff
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.parsers import load_file


def generate_diff(file1, file2, format_name='stylish'):
    data1 = load_file(file1) or {}
    data2 = load_file(file2) or {}

    if not data1 and not data2:
        if format_name == 'stylish':
            return "{}"
        return "{}"

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    raise ValueError(f"Unsupported format: {format_name}")
