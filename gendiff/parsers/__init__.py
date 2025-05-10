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


FIXTURES_DIR = Path(__file__).resolve().parent.parent / 'tests' / 'fixtures'


def load_file(path):
    path = Path(path).expanduser()

    if path.exists():
        actual_path = path.resolve()
    else:
        fixture_path = FIXTURES_DIR / path
        if fixture_path.exists():
            actual_path = fixture_path.resolve()
        else:
            raise FileNotFoundError(f"File not found: {path}")

    try:
        content = actual_path.read_text(encoding='utf-8')
        return parse_content(content, actual_path.suffix)
    except Exception as e:
        raise ValueError(f"Error reading {actual_path}: {str(e)}")