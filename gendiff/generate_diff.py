#!/usr/bin/env python3

from gendiff.scripts.read_parse import parse_file


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1, 'json')
    data2 = parse_file(file_path2, 'json')

    result = '{\n'
    keys_data1 = set(data1.keys())
    keys_data2 = set(data2.keys())
    combined_keys = sorted(keys_data1.union(keys_data2))

    for key in combined_keys:
        if key not in data2:
            result += f' - {key}: {data1[key]}\n'

        elif key not in data1:
            result += f' + {key}: {data2[key]}\n'

        elif data1[key] != data2[key]:
            result += f' - {key}: {data1[key]}\n'
            result += f' + {key}: {data2[key]}\n'

        else:
            result += f'   {key}: {data1[key]}\n'

    result += '}'
    return result
