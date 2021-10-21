#!/usr/bin/python3.8
# --------------------------------------------------
# A python script for printing if the numbers until maximum_number are prime
# Rafael Inacio Siopa.
# PSR, October 2021.
# --------------------------------------------------

import readchar
from colorama import Fore, Back, Style

def printAllCharsUpTo(stop_char):

    """
    Reads a character from the keyboard and prints all the characters from
    the space ' ' until that character (following the ASCII table)
    :param stop_char: character to read
    :return: none
    """

    for i in range(ord(' '), ord(stop_char)):
        print(i)


def readAllUpTo(stop_char):

    """
    Reads a character from the keyboard and reads all the following characters
    until it reads the original character again
    :param stop_char: character to read
    :return: none
    """

    c2 = readchar.readchar()
    while c2 != stop_char:
        c2 = readchar.readchar()


def countNumbersUpTo(stop_char):

    """
    Reads a character from the keyboard and reads all the following characters
    until it reads the original character again, printing the number of numbers
    read and the number of other characters read
    :param stop_char: character to read
    :return: total of numbers read and total of "not a number"s read
    """

    input_list = []
    input_list_numeric = []
    input_list_other = []
    diction_other = {}

    while True:

        c = readchar.readchar()

        if c == stop_char:
            break

        input_list.append(c)

    total_numbers = 0
    total_others = 0
    total_pressed = 0

    """
    while True:
        c3 = readchar.readchar()
        if c3 == stop_char:
            break
        elif c3.isnumeric():
            total_numbers += 1
        elif not c3.isnumeric():
            total_others += 1
    """

    input_list_numeric = [x for x in input_list if x.isdigit()]

    for idx_pressed_key, input in enumerate(input_list):
        if input.isnumeric():
            #input_list_numeric.append(input)
            total_numbers += 1
        else:
            total_others += 1
            input_list_other.append(input)
            diction_other[idx_pressed_key] = input

    input_list_numeric.sort()
    #use set function to make another sorted list but with no repetition of numbers

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')
    print(diction_other)

    # CHALLENGE

    colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW]

    print('Colored text:')

    count = 0
    txt_color = ''

    for others in input_list_other:
        txt_color = txt_color + colors[count] + others + Style.RESET_ALL
        count += 1
        if count > len(colors)-1:
            count = 0

    print(txt_color)

def main():

    c = readchar.readchar()
    #printAllCharsUpTo(c)
    #readAllUpTo(c)
    countNumbersUpTo(c)


if __name__ == '__main__':
    main()
