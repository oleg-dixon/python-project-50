#!/usr/bin/env python3
import argparse

from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    # Позиционные аргументы
    parser.add_argument(
        'first_file',
        metavar='first_file'
    )
    parser.add_argument(
        'second_file',
        metavar='second_file'
    )

    # Опциональные аргументы
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        help='set format of output',
        default='json'
    )

    args = parser.parse_args()
    print(generate_diff(
        args.first_file,
        args.second_file,
        format_name=args.format
    ))


if __name__ == '__main__':
    main()
    