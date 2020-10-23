def addition(a, b):
    return a + b


def subtraction(a, b):
    return b - a


def multiplication(a, b):
    return a * b


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
