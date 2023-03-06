import time

operacoes = ["soma", "subtracao", "multiplicacao", "divisao"]

def operacao(n1, n2):
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
    if sinal != operacoes:
        return ("Opção inválida!")

while True:
    n1 = float(input("Digite o primeiro número: "))
    sinal = input("Agora digite o sinal, dentre as seguintes opções: soma: + subtracao: - multiplicacao: * divisao: / : ")
    n2 = float(input("Digite o segundo número: "))
        

    if n2 == 0 and sinal == "/" or sinal == "divisao":
        print("Não é possível dividir por 0")
        time.sleep(1)
        continue
    
    sinal = sinal.strip()
    sinal = sinal.lower()
    print(operacao(n1, n2))