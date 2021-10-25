#!/usr/bin/python3.8
# --------------------------------------------------
# A python script for complex number operations
# Rafael Inacio Siopa.
# PSR, October 2021.
# --------------------------------------------------


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
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))


if __name__ == '__main__':
    main()
