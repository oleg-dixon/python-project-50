#!/usr/bin/env python3

from gendiff.scripts.read_parse import parse_file


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1, 'json')
    data2 = parse_file(file_path2, 'json')

    result = ['{']
    keys_data1 = set(data1.keys())
    keys_data2 = set(data2.keys())
    combined_keys = sorted(keys_data1.union(keys_data2))

    for key in combined_keys:
        if key not in data2:
            result.append(f' - {key}: {format_value(data1[key])}')
        elif key not in data1:
            result.append(f' + {key}: {format_value(data2[key])}')
        elif data1[key] != data2[key]:
            result.append(f' - {key}: {format_value(data1[key])}')
            result.append(f' + {key}: {format_value(data2[key])}')
        else:
            result.append(f'   {key}: {format_value(data1[key])}')

    result.append('}')
    return '\n'.join(result)
