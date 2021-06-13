"""
# USO BÁSICO DE PRINT Y VARIABLES
age = 17
text = "Carlos David Ramírez Muñoz"
print("Hi, my name is \'" + text + "\'\nI am " + str(age) + "\n")
print(3 ** 2)

# OBTENER INPUT DEL USUARIO
a = input("Enter a number:")
b = input("Enter another number:")
print("* The result is", float(a)+float(b))

# LISTAS BÁSICAS
sublist = [2, 3]
list = [0, -2, 3, 2, sublist]
print(list[4][1])

# AÑADE UNA LISTA CON OTRA
numbers.extend(names)

# MANEJO DE ARRAYS
print(numbers[:4])
# The same as numbers += names
# numbers.extend(names)
# numbers[:3] = [1, 2, 3]
numbers.append("sd")
numbers = [2, 3, 5, 1, -2]
names = [234, "Luz", "XD", "LUL"]
numbers.insert(3, 4)
numbers.insert(8, 6)
print(numbers)

# COMPRENSIÓN DE LISTAS
newList = [x for x in range(1, 11)]
print(newList)

# ORDENAR ARRAYS
newList = [3, 2, 1, 9, 2]
newList.sort()
print(newList)

# CONJUNTOS
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# DICCIONARIOS
pc = {
    "model": "Modelo xd",
    "brand": "Asus",
    "processor": "Ryzen 7"
}
## Obtener atributos objetos
print(pc["model"])
print(pc["model"])
print(pc.get("model"))
"""
pc = {
    "model": "Modelo xd",
    "brand": "Asus",
    "processor": "Ryzen 7"
}
pc["model"] = "ROG"
pc["ram"] = 8
pc.pop("brand")
print("atributos: {}".format(pc.keys()))
print("valores: {}".format(pc.values()))
print("items: {}".format(pc.items()))
for x in pc:
    print(pc[x])
