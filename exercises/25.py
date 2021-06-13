def isInArray(element, array):
    if element in array:
        print(element, "it's in the array")
    else:
        print(element, "it's not in the array")


listA = [2, "xs", 4, 23]
x = input("Please enter the element")
isInArray(x, listA)
