"""
SOLUCION QUE DI INICIALMENTE

numbers = str(input("Enter a number list separated by a comma: "))
numberString = str()
numberTuple = tuple()
numberList = list()
for character in numbers:
    if(character == "0" or character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6" or character == "7" or character == "8" or character == "9"):
        numberString += character
    elif(character == ","):
        numberList.append(int(numberString))
        numberString = str()
numberList.append(int(numberString))
numberTuple = numberList.copy()
print("List:", numberList)
print("Tuple:", numberTuple)
"""
# SOLUCION MÁS EFICIENTE

numbers = str(input("Enter a number list separated by a comma: "))
numberList = numbers.split(",")
numberTuple = tuple(values)
print("List:", numberList)
print("Tuple:", numberTuple)
