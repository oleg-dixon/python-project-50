import json
import os

import pytest

from gendiff import generate_diff

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


@pytest.mark.parametrize("file1, file2, expected_file, format_name", [
    ('file1.json', 'file2.json', 'expected_stylish.txt', 'stylish'),
    ('file1.yaml', 'file2.yaml', 'expected_stylish.txt', 'stylish'),
    ('file1.json', 'file2.json', 'expected_json.json', 'json'),
    ('empty1.json', 'empty2.json', 'expected_empty.txt', 'stylish'),
])
def test_generate_diff(file1, file2, expected_file, format_name):
    file1_path = os.path.join(FIXTURES_DIR, file1)
    file2_path = os.path.join(FIXTURES_DIR, file2)
    expected_path = os.path.join(FIXTURES_DIR, expected_file)

    with open(expected_path) as f:
        expected = f.read().strip()

    result = generate_diff(file1_path, file2_path, format_name).strip()

    if format_name == 'json':
        assert json.loads(result) == json.loads(expected)
    else:
        assert result == expected
