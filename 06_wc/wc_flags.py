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
def total_output(line_total, word_total, byte_total,
                 lines, words, chars, any_flags_set):
    """Outputs total to console"""

    output = ''
    if lines or not any_flags_set:
        output += f'{line_total:8}'
    if words or not any_flags_set:
        output += f'{word_total:8}'
    if chars or not any_flags_set:
        output += f'{byte_total:8}'
    print(output + ' total')


# --------------------------------------------------
def get_file_column_count(fh, text_output, column_count, column_total):
    """Returns count as string output and number"""

    column_total += column_count
    text_output += f'{column_count:8}'
    fh.close()
    return text_output, column_total


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    any_flags_set = args.lines or args.words or args.chars

    line_total, word_total, byte_total = 0, 0, 0

    for fh in args.file:
        text_output = ''
        line_count, word_count, byte_count = 0, 0, 0
        for line in fh:
            if args.lines or not any_flags_set:
                line_count += 1
            if args.words or not any_flags_set:
                word_count += len(line.split())
            if args.chars or not any_flags_set:
                byte_count += len(line)
        if args.lines or not any_flags_set:
            text_output, line_total = get_file_column_count(fh, text_output, line_count, line_total)
        if args.words or not any_flags_set:
            text_output, word_total = get_file_column_count(fh, text_output, word_count, word_total)
        if args.chars or not any_flags_set:
            text_output, byte_total = get_file_column_count(fh, text_output, byte_count, byte_total)
        print(text_output + ' ' + fh.name)
        fh.close()

    if len(args.file) > 1:
        total_output(line_total, word_total, byte_total,
                     args.lines, args.words, args.chars,
                     any_flags_set)


# --------------------------------------------------
if __name__ == '__main__':
    main()
