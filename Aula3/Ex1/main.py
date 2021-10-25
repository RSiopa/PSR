#!/usr/bin/python3.8
# --------------------------------------------------
# A python script that prints the time it takes to do the square root of the numbers from 1 to 50 million
# Rafael Inacio Siopa.
# PSR, October 2021.
# --------------------------------------------------

from colorama import Fore, Back, Style
from time import time, ctime
import math


def main():

    t1 = time()
    for i in range(1, 50000000):
        math.sqrt(i)
    t2 = time()

    t_total = t2 - t1
    ct = ctime()

    print('This is ' + Fore.RED + 'Ex1 ' + Style.RESET_ALL + 'and the current date is ' +
          Back.YELLOW + ct + Style.RESET_ALL)
    print('Elapsed time ' + str(t_total) + ' seconds.')


if __name__ == '__main__':
    main()
