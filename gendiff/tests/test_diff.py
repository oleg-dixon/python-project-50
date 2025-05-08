import os

import pytest

from gendiff.generate_diff import generate_diff

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


@pytest.mark.parametrize(
    "file1,file2,expected_file",
    [
        (
            os.path.join(FIXTURES_DIR, 'file1.json'),
            os.path.join(FIXTURES_DIR, 'file2.json'),
            os.path.join(FIXTURES_DIR, 'expected_stylish.txt'),
        ),
        (
            os.path.join(FIXTURES_DIR, 'file1.yaml'),
            os.path.join(FIXTURES_DIR, 'file2.yaml'),
            os.path.join(FIXTURES_DIR, 'expected_stylish.txt'),
        ),
    ]
)
def test_generate_diff_stylish(file1, file2, expected_file):
    """
    Тестирует генерацию различий для файлов в формате 'stylish'.
    
    :param file1: путь к первому файлу
    :param file2: путь ко второму файлу
    :param expected_file: путь к ожидаемому результату
    """
    with open(expected_file, 'r') as f:
        expected = f.read().strip()

    result = generate_diff(file1, file2, format_name='stylish')
    assert result.strip() == expected, (
    f'Expected:\n{expected}\n\nGot:\n{result}'
    )


@pytest.mark.parametrize('format', ['json', 'yaml', 'yml'])
def test_generate_diff(format):
    """
    Тестирует функцию generate_diff для разных форматов данных.
    
    :param format: формат файлов для теста (json, yaml, yml)
    """
    base_path = 'gendiff/tests/fixtures'
    with open(os.path.join(base_path, 'expected_output.txt')) as f:
        expected = f.read()
    file1 = os.path.join(base_path, f'file1.{format}')
    file2 = os.path.join(base_path, f'file2.{format}')
    result = generate_diff(file1, file2, format_name='stylish')
    assert expected == result, f'Expected:\n{expected}\n\nGot:\n{result}'


@pytest.mark.parametrize('format', ['json', 'yaml', 'yml'])
def test_generate_diff_empty_files(format):
    """
    Тестирует генерацию различий для пустых файлов.
    
    :param format: формат файлов для теста (json, yaml, yml)
    """
    base_path = 'gendiff/tests/fixtures'
    with open(os.path.join(base_path, 'expected_empty_files.txt')) as f:
        expected = f.read()
    file1 = os.path.join(base_path, f'empty_file1.{format}')
    file2 = os.path.join(base_path, f'empty_file2.{format}')
    result = generate_diff(file1, file2)
    assert expected == result, f'Expected:\n{expected}\n\nGot:\n{result}'


@pytest.mark.parametrize('format', ['json', 'yaml', 'yml'])
def test_generate_diff_large_files(format):
    """
    Тестирует генерацию различий для больших файлов.
    
    :param format: формат файлов для теста (json, yaml, yml)
    """
    base_path = 'gendiff/tests/fixtures'
    with open(os.path.join(base_path, 'expected_large_file_stylish.txt')) as f:
        expected = f.read()
    file1 = os.path.join(base_path, f'large_file1.{format}')
    file2 = os.path.join(base_path, f'large_file2.{format}')
    result = generate_diff(file1, file2)
    assert expected == result, f'Expected:\n{expected}\n\nGot:\n{result}'
