import math

a = float(input("Primeiramente, digite o valor a: "))
b = float(input("Agora, o valor b: "))
c = float(input("Agora, o valor c: "))
delta = ((b ** 2) - (4 * a * c))

while True:
    try:
        if delta < 0:
            print ("Delta negativo.")
        else:
            raiz = math.sqrt(delta)
            pis = ((-b)) 
            divis = (2 * a)
            raizum = (pis + raiz) / divis
            raizdois = (pis - raiz) / divis
        if raizdois == raizum:
            print(f"A raiz é: {round(raizum, 2)}")
        else:
            print(f"A raiz um é: {round(raizum, 2)} A raiz dois é: {round(raizdois, 2)}")
    except ValueError:
        print("Sinal invalido.")
    else:
        break


