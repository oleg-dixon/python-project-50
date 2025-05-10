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
    try:
        with open(path, 'r') as file:
            content = file.read()
            extension = Path(path).suffix
            return parse_content(content, extension)
    except FileNotFoundError:
        raise ValueError(f"File not found: {path}")
    except Exception as e:
        raise ValueError(f"Error reading {path}: {str(e)}")
