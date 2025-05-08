import json


def parse_json(data):
    """Парсит JSON-строку в словарь Python."""
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")


def load_json(file_path):
    """Читает и парсит JSON-файл."""
    with open(file_path, 'r') as f:
        return parse_json(f.read())