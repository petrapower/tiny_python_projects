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

    parser.add_argument('-w',
                        '--words',
                        help='Print only number of words in input string or file',
                        action='store_true')

    parser.add_argument('-c',
                        '--chars',
                        help='Print only number of characters in input string or file',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    any_flags_true = args.lines or args.words or args.chars

    line_total, word_total, byte_total = 0, 0, 0

    for fh in args.file:
        item_output = ''
        line_count, word_count, byte_count = 0, 0, 0
        for line in fh:
            if args.lines or not any_flags_true:
                line_count += 1
            if args.words or not any_flags_true:
                word_count += len(line.split())
            if args.chars or not any_flags_true:
                byte_count += len(line)
        if args.lines or not any_flags_true:
            line_total += line_count
            item_output += f'{line_count:8}'
            fh.close()
        if args.words or not any_flags_true:
            word_total += word_count
            item_output += f'{word_count:8}'
            fh.close()
        if args.chars or not any_flags_true:
            byte_total += byte_count
            item_output += f'{byte_count:8}'
            fh.close()
        print(item_output + ' ' + fh.name)
        fh.close()

    if len(args.file) > 1:
        print(f'{line_total:8}{word_total:8}{byte_total:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
