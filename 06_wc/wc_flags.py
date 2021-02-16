#!/usr/bin/env python3
"""
Author : petra <petra@localhost>
Date   : 2021-02-13
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),   # type has to be readable file - already open for reading
                        default=[sys.stdin],            # default is STDIN - no need to open(), it's accessible
                        nargs='*')                      # zero or more args

    parser.add_argument('-l',
                        '--lines',
                        help='Print only number of lines in input string or file',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    line_total, word_total, byte_total = 0, 0, 0

    for fh in args.file:
        line_count, word_count, byte_count = 0, 0, 0
        for line in fh:
            if args.lines:
                line_count += 1
                continue
            line_count += 1
            word_count += len(line.split())
            byte_count += len(line)
        if args.lines:
            print(f'{line_count:8} {fh.name}')
            line_total += line_count
            continue
        print(f'{line_count:8}{word_count:8}{byte_count:8} {fh.name}')
        line_total += line_count
        word_total += word_count
        byte_total += byte_count
        fh.close()

    if len(args.file) > 1:
        print(f'{line_total:8}{word_total:8}{byte_total:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
