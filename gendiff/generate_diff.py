from gendiff.diff_tree import build_diff_tree
from gendiff.formatters.json import format_json
from gendiff.formatters.stylish import format_stylish
from gendiff.parsers import load_file


def generate_diff(file1, file2, format_name='stylish'):
    data1 = load_file(file1)
    data2 = load_file(file2)

    if data1 is None:
        data1 = {}
    if data2 is None:
        data2 = {}

    diff_tree = build_diff_tree(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff_tree)
    elif format_name == 'json':
        return format_json(diff_tree)
    else:
        raise ValueError(f"Unsupported format: {format_name}")
