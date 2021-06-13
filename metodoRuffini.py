print("--- DIVISIÓN SINTÉTICA ----\n")
error = False  # En caso de error esta variable se vuelve True
factorizacionParcial = False
grado = int(input("* Ingresa el grado de tu ecuación:"))
while(grado <= 0):
    print("* Porfavor, ingresa un número entero positivo")
    grado = int(input("* Ingresa el grado de tu ecuación:"))
coeficientes = []
for i in range(grado, -1, -1):
    print("* Ingresa el coeficiente de la incógnita con grado", i)
    coeficienteX = int(input())
    coeficientes.append(coeficienteX)
# Utiliza factor comun lo máximo posible
exponenteFactorComun = 0
while coeficientes[len(coeficientes)-1] == 0:
    exponenteFactorComun += 1
    coeficientes.pop()

a0 = coeficientes[len(coeficientes)-1]
aN = coeficientes[0]

divisoresA0 = []
divisoresAN = []
# Encuentra los divisores de a0 y aN
for i in range(1, abs(a0)+1):
    if(a0 % i == 0):
        divisoresA0.append(i)
for i in range(1, abs(aN)+1):
    if(aN % i == 0):
        divisoresAN.append(i)
# Encuentra las posibles soluciones
posiblesX = []
for x0 in divisoresA0:
    for xN in divisoresAN:
        posiblesX.append(x0/xN)
# se agregan posibles soluciones negativas
posiblesXNegativos = []
for x in posiblesX:
    posiblesXNegativos.append(-x)
posiblesX.extend(posiblesXNegativos)

soluciones = []
nuevoPolinomio = []
aplicableARuffini = False
# Se usa Ruffini hasta que el polinomio sea de grado 1

while len(coeficientes) > 2:
    aplicableARuffini = True
    nuevoPolinomio = []
    posicionArrayPosiblesX = -1
    for posibleX in posiblesX:  # Se itera cada posible X en cada coeficiente
        posicionArrayPosiblesX += 1
        nuevoPolinomio = []
        posicionArrayCoeficientes = -1
        for coeficiente in coeficientes:
            posicionArrayCoeficientes += 1
            if(posicionArrayCoeficientes == 0):
                # En el primer paso de Ruffini el primer coeficiente no es afectado y pasa al nuevo polinomio
                suma = coeficientes[0]
            else:
                sustraendo = suma*posibleX  # Si no es el primer paso se realiza la operacion normal
                suma = coeficiente + sustraendo
            # Se va construyendo el posible nuevo polinomio
            nuevoPolinomio.append(suma)
        # Se verifica si el ultimo numero del nuevo polinomio es 0
        if(nuevoPolinomio[len(nuevoPolinomio)-1] == 0):
            soluciones.append(posibleX)
            nuevoPolinomio.pop()
            # Se establece el nuevo polinomio como nuevo coeficiente
            coeficientes = nuevoPolinomio.copy()
            break
        elif posicionArrayPosiblesX == len(posiblesX)-1:
            factorizacionParcial = True
            break
        if posicionArrayCoeficientes == len(posiblesX)-1:
            print(
                "\n- No podemos factorizar tu polinomio con división sintética :(")
            error = True
            break

    if(error == True or factorizacionParcial == True):
        break
if error == False and aplicableARuffini == True and factorizacionParcial == False:
    # Se agrega la última solución
    soluciones.append(-coeficientes[1]/coeficientes[0])

    if(aplicableARuffini):
        print("* Las soluciones de tu ecuación son:", soluciones)
    print("* La factorización es:")
    if(exponenteFactorComun > 0):
        print("(x^{})".format(exponenteFactorComun), end="")
    if(coeficientes[0] == 1):
        for factor in soluciones:
            if(factor > 0):
                print("(x - {:.2f})".format(abs(factor)), end="")
            else:
                print("(x + {:.2f})".format(abs(factor)), end="")
    else:
        if(coeficientes[1] > 0):
            print(
                "({}x + {:.2f})".format(coeficientes[0], abs(coeficientes[1])), end="")
        else:
            print(
                "({}x - {:.2f})".format(coeficientes[0], abs(coeficientes[1])), end="")
        soluciones.pop()
        for factor in soluciones:
            if(factor > 0):
                print("(x - {:.2f})".format(abs(factor)), end="")
            else:
                print("(x + {:.2f})".format(abs(factor)), end="")

elif exponenteFactorComun > 0:
    print("(x^{})(".format(exponenteFactorComun), end="")
    posicionArray = -1
    for coeficiente in coeficientes:
        posicionArray += 1
        if(posicionArray != len(coeficientes)-1):
            print("{}x^{} + ".format(coeficiente,
                  (len(coeficientes)-1)-posicionArray), end="")
        else:
            print("{}x^{})".format(coeficiente,
                  (len(coeficientes)-1)-posicionArray))

elif(factorizacionParcial):
    for factor in soluciones:
        if(factor > 0):
            print("(x - {:.2f})".format(abs(factor)), end="")
        else:
            print("(x + {:.2f})".format(abs(factor)), end="")
    print("(", end="")
    posicionArray = -1
    for coeficiente in coeficientes:
        posicionArray += 1
        if(posicionArray != len(coeficientes)-1):
            print("{}x^{} + ".format(coeficiente,
                  (len(coeficientes)-posicionArray)), end="")
        else:
            print("{}x^{})".format(coeficiente,
                  (len(coeficientes)-posicionArray)), end="")
