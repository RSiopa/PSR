#!/usr/bin/python3.8
# --------------------------------------------------
# A python script for complex number operations using named tuples and classes
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------

import argparse

parser = argparse.ArgumentParser(description='Definition of test mode')
parser.add_argument('-utm', '--use_time_mode', help='The test runs for X seconds', action='store_true')
parser.add_argument('-mv', '--max_value', type=int, help='The test runs for MAX_VALUE inputs')
args = parser.parse_args()


def main():
    # print(args.max_value)
    if args.use_time_mode:
        print('hi')
    if type(args.max_value) == int:
        print('bye')


if __name__ == '__main__':
    main()