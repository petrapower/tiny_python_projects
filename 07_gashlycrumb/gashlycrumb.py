#!/usr/bin/env python3
"""
Author : petra <petra@localhost>
Date   : 2021-02-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        help='Letter(s)',
                        metavar='letter',
                        nargs='+',
                        type=str)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    letters_to_lines = {}
    for line in args.file:
        letters_to_lines[line[0].upper()] = line.rstrip()

    for letter in args.letter:
        print(letters_to_lines.get(letter.upper(), f'I do not know \"{letter}\".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
