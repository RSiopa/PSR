#!/usr/bin/python3.8
# --------------------------------------------------
# A python script for functions
# Rafael Inacio Siopa.
# PSR, October 2021.
# --------------------------------------------------

import math

def isPrime(value):

    """
    Checks whether the number value is Prime
    :param value: the number to test
    :return: True or False
    """

    print('\nReference number ' + str(value))

    if value == 0:
        return False
    elif value == 1:
        return False
    elif value == 2:
        return True

    for i in range(2, math.ceil(math.sqrt(value)) + 1):
        remainder = value % i
        print(str(value) + ' / ' + str(i) + ' has remainder ' + str(remainder))
        if remainder == 0:
            return False

    return True
