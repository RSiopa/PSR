#!/usr/bin/python3

from colorama import Fore, Back, Style

maximum_number = 50


def isPrime(value):

    print('\nReference number ' + str(value))

    for i in range(2, value):
        remainder = value % i
        print(str(value) + ' / ' + str(i) + ' has remainder ' + str(remainder))
        if remainder == 0:
            return False

    return True

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    counter = 0
    for i in range(0, maximum_number):
        if isPrime(i):
            counter = counter + 1
            print(Back.YELLOW + Fore.RED + Style.DIM + 'Number ' + Back.CYAN + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + str(i) + Back.YELLOW + Fore.RED + Style.DIM + ' is prime.' + Style.RESET_ALL)
        else:
            print('Number ' + str(i) + ' is not prime.')

    print(Fore.BLUE + 'Between 1 and ' + str(maximum_number) + ' we have ' + str(counter) + ' prime numbers.' + Style.RESET_ALL)

if __name__ == "__main__":
    main()