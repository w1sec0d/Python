"""
COMENTARIOS:

WHILE Y SINTAXIS BÁSICA

numero_a = 1
while numero <= 10:
    print(numero)
    numero += 1

num = 5
i = 0
texto = ""
while i < 5:
    texto += "*"
    print(texto)
    i += 1

FUNCIONES BÁSICAS

def saludar():
    print("Hola Pana")


def despedir(nombre="pana"):
    return "Adios "+nombre


saludo = int(input("Deseas que te salude? 1) SI 2) NO "))
while(saludo == 1):
    print("hola pana")
    print(despedir(input("Cual es tu nombre?")))
    saludo = int(input("Deseas que te salude? 1) SI 2) NO "))

TUPLAS() NO SE PUEDE CAMBIAR SU VALOR
"""
hanna = (17, 1.65, "Hanna")


def imprimirTupla(posicion=0):
    print(hanna[posicion])


imprimirTupla(int(input("Que posicion deseas imprimir?")))

for caracteristica in hanna:
    print(caracteristica)
