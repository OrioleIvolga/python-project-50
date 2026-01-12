# gendiff/scripts/gendiff.py

import argparse

from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='First file path')
    parser.add_argument('second_file', help='Second file path')
    # ← НЕТ аргумента -f/--format

    args = parser.parse_args()

    # Всегда используем формат 'stylish' (по умолчанию)
    result = generate_diff(args.first_file, args.second_file, 'stylish')
    print(result)


if __name__ == '__main__':
    main()
