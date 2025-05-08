from pathlib import Path

from gendiff.generate_diff import generate_diff


def get_fixture_path(file_name, file_format):
    if file_format == 'json':
        return Path(__file__).parent / 'test_data' / file_name
    if file_format in ('yml', 'yaml'):
        return Path(__file__).parent / 'test_data' / file_name


# test_cases = ["yml", "json"]


# @pytest.mark.parametrize("format", test_cases)
# def test_generate_diff(format):


def test_generate_diff_json():
    file1 = get_fixture_path('file1.json', 'json')
    file2 = get_fixture_path('file2.json', 'json')

    expected = """{
 - follow: false
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: true
}"""
    result = generate_diff(file1, file2)
    assert result == expected, f'Expected:\n{expected}\n\nGot:\n{result}'


def test_generate_diff_yaml():
    file1 = get_fixture_path('file1.yml', 'yml')
    file2 = get_fixture_path('file2.yaml', 'yaml')

    expected = """{
 - follow: false
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: true
}"""
    result = generate_diff(file1, file2)
    assert result == expected, f'Expected:\n{expected}\n\nGot:\n{result}'


def test_generate_diff_identical_files_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file1.json')

    expected = """{
   follow: false
   host: hexlet.io
   proxy: 123.234.53.22
   timeout: 50
}"""

    result = generate_diff(file1, file2)
    assert result == expected, f'Expected:\n{expected}\n\nGot:\n{result}'


def test_generate_diff_empty_files():
    file1 = get_fixture_path('empty1.json')
    file2 = get_fixture_path('empty2.json')

    expected = """{
}"""

    result = generate_diff(file1, file2)
    assert result == expected, f'Expected:\n{expected}\n\nGot:\n{result}'
