import time

def operacao(n1, n2):
    if sinal == "+" or sinal == "soma":
        resultado = n1 + n2
        return resultado
    elif sinal == "-" or sinal == "subtracao":
        resultado = n1 - n2
        return resultado
    elif sinal == "*" or sinal == "multiplicação":
        resultado = (n1 * n2)
        return resultado
    elif sinal == "/" or sinal == "divisão":
        resultado = n1 / n2
        return resultado

while True:
    try:
        n1 = float(input("Digite o primeiro número: "))
        sinal = input("Agora digite o sinal, dentre as seguintes opções: soma: + subtracao: - multiplicação: * divisão: / : ")
        n2 = float(input("Digite o segundo número: "))
        
    except ValueError:
        print("Opção inválida.")
        time.sleep(1.25)
    else:
        break

sinal = sinal.strip()
sinal = sinal.lower()
print(operacao(n1, n2))
alterado

