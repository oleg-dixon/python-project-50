from gendiff.parsers import load_file
from gendiff.engine import build_diff, format_diff


def generate_diff(file_path1, file_path2):
    """Генерирует различия между двумя файлами"""
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    diff = build_diff(data1, data2)
    return format_diff(diff)