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
    with open(expected_file, 'r') as f:
        expected = f.read().strip()

    result = generate_diff(file1, file2, format_name='stylish')
    assert result.strip() == expected
