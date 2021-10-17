#!/usr/bin/python3.8
# --------------------------------------------------
# A python script for printing if the numbers until maximum_number are prime
# Rafael Inacio Siopa.
# PSR, October 2021.
# --------------------------------------------------

import readchar

def printAllCharsUpTo(stop_char):

    """
    Reads a character from the keyboard and prints all the characters from
    the space ' ' until that character (following the ASCII table)
    :param value: character to read
    :return: none
    """

    for i in range(ord(' '), ord(stop_char)):
        print(i)


def readAllUpTo(stop_char):

    """
    Reads a character from the keyboard and reads all the following characters
    until it reads the original character again
    :param value: character to read
    :return: none
    """

    c2 = readchar.readchar()
    while c2 != stop_char:
        c2 = readchar.readchar()


def countNumbersUpTo(stop_char):
    total_numbers = 0
    total_others = 0
    while True:
        c3 = readchar.readchar()
        if c3 == stop_char:
            break
        elif c3.isnumeric():
            total_numbers += 1
        elif not c3.isnumeric():
            total_others += 1

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')


def main():

    c = readchar.readchar()
    #printAllCharsUpTo(c)
    #readAllUpTo(c)
    countNumbersUpTo(c)


if __name__ == '__main__':
    main()
