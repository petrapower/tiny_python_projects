#!/usr/bin/env python3
"""
Author : petra <petra@localhost>
Date   : 2021-02-15
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

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

    letters_to_lines = {line[0].upper(): line.rstrip() for line in args.file}

    print('Please provide a letter [! to quit]: ')
    for line in sys.stdin:
        user_in = line.upper().rstrip()
        if user_in == '!':
            print("Bye")
            break
        print(letters_to_lines.get(user_in.upper(), f'I do not know \"{user_in}\".'))
        print('Please provide a letter [! to quit]: ')


# --------------------------------------------------
if __name__ == '__main__':
    main()
