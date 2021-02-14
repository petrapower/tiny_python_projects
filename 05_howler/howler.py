#!/usr/bin/env python3
"""
Author : petra <petra@localhost>
Date   : 2021-02-09
Purpose: Rock the Casbah
"""

import argparse
import os.path
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    fh_out = open(args.outfile, 'wt') if args.outfile else sys.stdout
    fh_out.write(args.text.upper() + '\n')
    fh_out.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
