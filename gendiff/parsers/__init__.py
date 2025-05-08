import json
from pathlib import Path

import yaml


def parse_content(content, extension):
    """Парсит содержимое файла по его расширению"""
    if extension == '.json':
        return json.loads(content)
    elif extension in ('.yaml', '.yml'):
        return yaml.safe_load(content)
    raise ValueError(f"Unsupported file extension: {extension}")


def load_file(file_path):
    """Загружает и парсит файл"""
    path = Path(file_path)
    if not path.is_absolute():
        path = Path(__file__).parent.parent.parent / path
    with open(path) as f:
        content = f.read()
    return parse_content(content, path.suffix.lower())