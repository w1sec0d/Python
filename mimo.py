"""
import math


def timesPI(num):
    return num*math.pi


prices = [24, 23, 23, 1]
pricesPI = [timesPI(price) for price in prices]
print(pricesPI)
"""


class President:
    def __init__(self, name, hasBacon):
        self.name = name
        self.hasBacon = hasBacon

    def bark(self):
        print("oinc")


duque = President("Duque", True)

# ejemplo de FP a OPP


def getArea(base, height):
    return base*height


print(getArea(3, 5))


class Rectangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = base * height


a = Rectangle(3, 5)
print(a.area)
