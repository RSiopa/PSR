#!/usr/bin/env python
# --------------------------------------------------
# A python script for functions
# Rafael Inacio Siopa.
# PSR, October 2021.
# --------------------------------------------------

def isPrime(value):

    """
    Checks whether the number value is Prime
    :param value: the number to test
    :return: True or False
    """

    print('\nReference number ' + str(value))

    for i in range(2, value):
        remainder = value % i
        print(str(value) + ' / ' + str(i) + ' has remainder ' + str(remainder))
        if remainder == 0:
            return False

    return True
