#!/usr/bin/python3.8
# --------------------------------------------------
# A python script for complex number operations using named tuples and classes
# Rafael Inacio Siopa.
# PSR, October 2021.
# --------------------------------------------------


class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, y):
        c_sum = Complex(self.r + y.r, self.i + y.i)
        return c_sum

    def multiply(self, y):
        c_multiply = Complex(self.r*y.r - self.i*y.i, self.r*y.i + self.i*y.r)
        return c_multiply

    def __str__(self):
        return "{} + {}i".format(self.r, self.i)


def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant

    # Test add
    print(c1)  # uses the __str__ method in the class
    c3 = c1.add(c2)
    print(c3)  # uses the __str__ method in the class

    # test multiply
    print(c2)  # uses the __str__ method in the class
    c4 = c2.multiply(c1)
    print(c4)  # uses the __str__ method in the class


if __name__ == '__main__':
    main()