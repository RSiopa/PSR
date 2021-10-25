#!/usr/bin/python3.8
# --------------------------------------------------
# A python script for complex number operations using named tuples
# Rafael Inacio Siopa.
# PSR, October 2021.
# --------------------------------------------------

from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])


def addComplex(x, y):
    c_sum = (x[0] + y[0], x[1] + y[1])
    return c_sum


def multiplyComplex(x, y):
    c_multiply = (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
    return c_multiply


def printComplex(x):
    print(x[0], '+', x[1], 'i')


def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are named order is not relevant
    print('c1 = ' + str(c1)) # named tuple looks nice when printed

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))


if __name__ == '__main__':
    main()