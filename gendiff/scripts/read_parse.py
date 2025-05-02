import json

def read_file(file_path):
    """Читает и возвращает содержимое файла как строку."""
    with open(file_path, 'r') as file:
        return file.read()
    

def parse_data(data, file_path):
    """Парсит строку данных в зависимости от указанного формата."""
    if file_path == 'json':
        return json.loads(data)


def parse_file(file_path, file_format):
    """Комбинированная функция чтения и парсинга файла."""
    data = read_file(file_path)
    return parse_data(data, file_format)
