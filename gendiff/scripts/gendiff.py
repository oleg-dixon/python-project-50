#!/usr/bin/env python

import argparse

from gendiff.generate_diff import generate_diff


def main():

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument(
        'first_file',
        help='path to the first file'
    )
    parser.add_argument(
        'second_file',
        help='path to the second file'
    )

    parser.add_argument(
        '-f', '--format',
        help='set format of output'
    )
    
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file))
  

if __name__ == '__main__':
    main()
