from gendiff.diff_tree import build_diff_tree
from gendiff.formatters.stylish import format_stylish
from gendiff.parsers import load_file


def generate_diff(file1, file2):
    data1 = load_file(file1)
    data2 = load_file(file2)

    print(f"Data from file1: {data1}")
    print(f"Data from file2: {data2}")

    diff_tree = build_diff_tree(data1, data2)
    return format_stylish(diff_tree)

