#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff


def main():
    # Создаем кастомный форматтер для help
    class CustomHelpFormatter(argparse.HelpFormatter):
        def _format_action(self, action):
            # Для позиционных аргументов убираем текст help
            if not action.option_strings:
                return super()._format_action(argparse.Action(
                    action.option_strings,
                    action.dest,
                    help=argparse.SUPPRESS,
                    metavar=action.metavar
                ))
            return super()._format_action(action)

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        formatter_class=CustomHelpFormatter,
        add_help=False  # Отключаем стандартный help
    )

    # Позиционные аргументы (без текста help)
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
        '-h', '--help',
        action='help',
        help='show this help message and exit'
    )
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        help='set format of output'
    )

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
    