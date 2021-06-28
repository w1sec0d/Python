a = int(input("Please enter a positive integer"))
b = int(input("Please enter a positive integer"))
aMultiples = list()
bMultiples = list()
numeroHallado = False
x = 1
while numeroHallado == False:
    aMultiples.append(a*x)
    bMultiples.append(b*x)
    for number in aMultiples:
        if number in bMultiples:
            numeroHallado = number
    x += 1
print("The least common multiple is: {}".format(numeroHallado))
