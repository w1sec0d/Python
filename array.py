persona = (17, 1.7, "Carlos")
# print(persona[0])

i = 0
print("Recorrer array con while")
while(i < len(persona)):
    print(persona[i])
    i += 1
print("")
print("Recorrer array con for")
for index in persona:
    print(index)
