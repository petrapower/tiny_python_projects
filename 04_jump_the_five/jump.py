#!/usr/bin/env python3
"""
Author : petra <petra@localhost>
Date   : 2021-02-06
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    encoded_nums = {"1": "9",
                    "2": "8",
                    "3": "7",
                    "4": "6",
                    "5": "0",
                    "6": "4",
                    "7": "3",
                    "8": "2",
                    "9": "1",
                    "0": "5"}

    for char in args.text:
        print(encoded_nums.get(char, char), end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
