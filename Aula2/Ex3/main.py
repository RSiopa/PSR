#!/usr/bin/python3.8
# --------------------------------------------------
# A python script for printing if the numbers until maximum_number are prime
# Rafael Inacio Siopa.
# PSR, October 2021.
# --------------------------------------------------

import argparse
from my_functions import isPrime
from colorama import Fore, Back, Style

parser = argparse.ArgumentParser()
parser.add_argument('--max_number', type=int)
args = parser.parse_args()

maximum_number = args.max_number


def main():

    print("Starting to compute prime numbers up to " + str(maximum_number))

    counter = 0
    for i in range(0, maximum_number):
        if isPrime(i):
            counter = counter + 1
            print(Back.YELLOW + Fore.RED + Style.DIM + 'Number ' + Back.CYAN + Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
                  str(i) + Back.YELLOW + Fore.RED + Style.DIM + ' is prime.' + Style.RESET_ALL)
        else:
            print('Number ' + str(i) + ' is not prime.')

    print(Fore.BLUE + 'Between 1 and ' + str(maximum_number) + ' we have ' + str(counter) + ' prime numbers.' +
          Style.RESET_ALL)


if __name__ == "__main__":
    main()
