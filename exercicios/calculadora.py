import time

def operacao(n1, n2, sinal):
    if sinal == "+" or sinal == "soma":
        resultado = n1 + n2
        return resultado
    elif sinal == "-" or sinal == "subtracao":
        resultado = n1 - n2
        return resultado
    elif sinal == "*" or sinal == "multiplicacao":
        resultado = (n1 * n2)
        return resultado
    elif sinal == "/" or sinal == "divisao":
        resultado = n1 / n2
        return resultado
    else:
        return ("Opção inválida!")

while True:
    try:
        n1 = float(input("Digite o primeiro número: "))
        sinal = input("Agora digite o sinal, dentre as seguintes opções: soma: + subtracao: - multiplicacao: * divisao: / : ")
        while sinal not in ["+", "-", "*", "/", "soma", "subtracao", "multiplicacao", "divisao"]:
            sinal = input("Sinal inválido. Por favor, digite um sinal válido: ")
            continue
        while True:
            try:
                n2 = float(input("Digite o segundo número: "))
                break
            except ValueError:
                print("Por favor, digite um número válido.")
                continue

    except ValueError:
        print("Por favor, digite um número válido.")
        continue
        

    if n2 == 0 and sinal == "/" or sinal == "divisao":
        print("Não é possível dividir por 0")
        time.sleep(1)
        continue
    
    sinal = sinal.strip()
    sinal = sinal.lower()
    print(operacao(n1, n2, sinal))