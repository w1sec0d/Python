"""
hora = 0
minu = 1
dura = 2939
horaFinal = (hora + (dura + minu)//60) % 24
minutoFinal = (dura + minu) % 60
print(horaFinal, ":", minutoFinal)

miLista = [1, 2, 10, 3, 5, 10, 4, 10]
# 8 elementos
# range(0,7) = 0 hasta 6
for elemento in miLista:
    if elemento == 10:
        miLista.pop(miLista.index(elemento))
print(miLista)

miLista = [1, 2]
(uno, dos) = miLista
print(uno)
"""
miLista = [1, 2, 3, 4, 10, 5, 6, 7, 5, 8, 9, 10, 10]

miListaSinRepetidos = [
    numero for numero in miLista if miLista.count(numero) == 1]
print(miListaSinRepetidos)
