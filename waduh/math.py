import math


def aritmethic(x, y, type=str):
    """
    Do a Aritmethic operation to number.

    Args:
      x (int, float): first number.
      y (int, float): second number.
      type= (string): operation type (add, substract, multiply, distribute)

    Returns:
      int, float: Result for aritmethic operation between x and y.
    """
    if type == "add":
        return x + y
    elif type == "substract":
        return x - y
    elif type == "multiply":
        return x * y
    elif type == "distribute":
        return x / y


def square(x, type=str):
    if type == "area":
        return x**2
    elif type == "perimeter":
        return 4 * x


def rectangle(x, y, type=str):
    if type == "area":
        return x * y
    elif type == "perimeter":
        return 2 * (x + y)


def triangle(x, y, z, type=str):
    if type == "area":
        return 0.5 * x * y
    elif type == "perimeter":
        return x + y + z


def circle(x, type=str):
    if type == "area":
        return math.pi * x**2
    elif type == "perimeter":
        return 2 * math.pi * x
