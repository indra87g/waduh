import math


class Arithmetic:
    def __init__(self, method=str):
        self.set_method(method)

    def set_method(self, method):
        if method == "add":
            self.method = self.add
        elif method == "multiply":
            self.method = self.multiply
        elif method == "substract":
            self.method = self.substract
        elif method == "distribute":
            self.method = self.distribute
        else:
            raise ValueError("Invalid arithmetic method.")

    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def substract(self, x, y):
        return x - y

    def distribute(self, x, y):
        if y == 0:
            raise ValueError("Distribute with zero is not allowed.")
        return x / y

    def calculate(self, x, y):
        return self.method(x, y)
