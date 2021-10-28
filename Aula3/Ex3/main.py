#!/usr/bin/python3.8
# --------------------------------------------------
# A python script for complex number operations using named tuples
# Rafael Inacio Siopa.
# PSR, October 2021.
# --------------------------------------------------

from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])


def addComplex(x, y):
    c_sum = Complex(x.r + y.r, x.i + y.i)
    return c_sum


def multiplyComplex(x, y):
    c_multiply = Complex(x.r*y.r - x.i*y.i, x.r*y.i + x.i*y.r)
    return c_multiply


def printComplex(x):
    print(x.r, '+', x.i, 'i')


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