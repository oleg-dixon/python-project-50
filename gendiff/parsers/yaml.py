import yaml


def parse_yaml(data):
    """Парсит YAML-строку в словарь Python."""
    try:
        return yaml.safe_load(data)
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML: {e}")


def load_yaml(file_path):
    """Читает и парсит YAML-файл."""
    with open(file_path, 'r') as f:
        return parse_yaml(f.read())