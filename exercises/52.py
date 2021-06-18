def print2(*strings, separator):
    stringPosition = -1
    for x in strings:
        stringPosition += 1
        if stringPosition == len(strings)-1:
            print(x)
        else:
            print(x + separator, end="")


print2("sda", "sadsad", separator="--")
