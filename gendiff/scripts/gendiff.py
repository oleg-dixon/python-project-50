import argparse


def main():
    # Создаем объект ArgumentParser с описанием
    parser = argparse.ArgumentParser(
        description = 'Compares two configuration files and shows a difference.'
    )

    # Добавляем позиционные аргументы
    parser.add_argument(
        'first_file',
        help = 'path to the first file'
    )
    parser.add_argument(
        'second_file',
        help = 'path to the second file'
    )

    # Аргумент -h уже добавлен по умолчанию через add_help=True в ArgumentParser
    # Поэтому, дополнительных настроек не требуется

    # Добавляем опциональный аргумент для формата
    parser.add_argument(
        '-f', '--format',
        help = 'set format of output'
    )

    # Парсим аргументы
    args = parser.parse_args()

    # Точка входа для логики приложения
    # Например, можно вызвать функцию для сравнения файлов
    # Например: compare_files(args.first_file, args.second_file)

if __name__ == '__main__':
    main()
