def stringToNumber(string):
    number = float(string)
    if number % 1 == 0:
        number = int(number)
    return number


print(stringToNumber("4.342"), type(stringToNumber("4.342")))
print(stringToNumber("4"), type(stringToNumber("4")))
print(stringToNumber("4.00"), type(stringToNumber("4.00")))
