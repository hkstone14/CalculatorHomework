def addition(a, b):
    return a + b


def subtraction(a, b):
    return b - a


def multiplication(a, b):
    return a * b


def division(a, b):
    return b / a


def square(a):
    return a * a


def squareroot(a):
    return a ** (1 / 2)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        a = int(a)
        b = int(b)
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        a = int(a)
        b = int(b)
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        a = int(a)
        b = int(b)
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        a = float(a)
        b = float(b)
        temp = 0
        temp = division(a, b)
        self.result = float('%.9f' % temp)
        return self.result

    def square(self, a):
        a = int(a)
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        a = float(a)
        temp = 0
        temp = squareroot(a)
        self.result = float('%.10g' % temp)
        return self.result
