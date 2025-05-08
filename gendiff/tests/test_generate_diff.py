import os
from pathlib import Path

import pytest

from gendiff.generate_diff import generate_diff


def get_fixture_path(file_name, file_format):
    if file_format == 'json':
        return Path(__file__).parent / 'test_data' / file_name
    if file_format in ('yml', 'yaml'):
        return Path(__file__).parent / 'test_data' / file_name


test_cases = ['yml', 'yaml', 'json']


@pytest.mark.parametrize('format', test_cases)
def test_generate_diff(format):
    base_path = 'gendiff/tests/test_data'
    with open(os.path.join(base_path, 'expected_output.txt')) as f:
        expected = f.read()
    file1 = os.path.join(base_path, f'file1.{format}')
    file2 = os.path.join(base_path, f'file2.{format}')
    result = generate_diff(file1, file2)
    assert expected == result, f'Expected:\n{expected}\n\nGot:\n{result}'
