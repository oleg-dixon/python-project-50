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


def load_file(path):
    with open(path, 'r') as file:
        content = file.read()
        if path.endswith('.json'):
            return json.loads(content)
        elif path.endswith('.yaml') or path.endswith('.yml'):
            return yaml.safe_load(content)
        else:
            raise ValueError(f"Unsupported file format: {path}")

