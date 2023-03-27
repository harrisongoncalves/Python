import time
from exercicios.POO_operacao import Operacao
operacao = Operacao()

def continuar():
    while True: 
        novamente = input("Deseja realizar outro cálculo? (s/n): ")
        if novamente == 'n':
            sair()
        elif novamente == 's':
            main()
        else:
            print("Opção inválida.")
            continue
    
def sair():
    print("Obrigado por utilizar o meu programa.")
    time.sleep(1.5)
    exit()

def main():
    while True:
        try:
            n1 = float(input("Digite o primeiro número: ").replace(",", "."))
            sinal = input("Agora digite o sinal, dentre as seguintes opções: soma: + subtracao: - multiplicacao: * divisao: / : ")
            while sinal not in ["+", "-", "*", "/", "soma", "subtracao", "multiplicacao", "divisao"]:
                sinal = input("Sinal inválido. Por favor, digite um sinal válido: ")
                continue
            while True:
                try:
                    n2 = float(input("Digite o segundo número: ").replace(",", "."))
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
    
        continuar()
main()