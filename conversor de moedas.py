import time
import requests

### futuramente tratar os erros requests

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,EUR-USD,BRL-USD,USD-EUR,BRL-EUR")
cotacoes = cotacoes.json()

### valor das cotacoes

cotacao_dolar_para_real = float(cotacoes['USDBRL']["bid"])
cotacao_euro_para_real = float(cotacoes['EURBRL']["bid"])
cotacao_real_para_dolar = float(cotacoes['BRLUSD']["bid"])
cotacao_real_para_euro = float(cotacoes['BRLEUR']['bid'])
cotacao_euro_para_dolar = float(cotacoes['EURUSD']["bid"])
cotacao_dolar_para_euro = float(cotacoes['USDEUR']["bid"])

def continuar():
    while True: 
        novamente = input("Deseja realizar outra conversão? (s/n): ")
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
    print("Conversor de moedas")
    print(f"US$ = R$ {cotacao_dolar_para_real:.2f} | EUR€ = R$ {cotacao_euro_para_real:.2f}\n")
    print("Selecione a opção de conversão:")
    print("1 --> Real para dólar\n"
    "2 --> Dólar para real\n"
    "3 --> Real para euro\n"
    "4 --> Euro para real\n"
    "5 --> Dólar para euro\n"
    "6 --> Euro para dólar\n"
    "7 --> Sair do programa")
    
    while True:
        try:
            moeda = int(input("Digite a sua opção: "))
        except ValueError:
            print("Opção inválida, escolha entre 1 e 7.")
            time.sleep(1)
            continue
            
        if moeda == 1:
            while True:
                try:
                    realdolarA = float(input("Digite o valor que você quer transformar em dólar: R$ "))
                    realdolar = float(realdolarA) * float(cotacao_real_para_dolar)
                    print(f"Você possui: U$ {realdolar:.2f}")
                    time.sleep(0.5)
                    continuar()
                except ValueError:
                    print("Número inválido.")
                    time.sleep(1)
                    continue
                


        if moeda == 2:
            while True:
                try:
                    dolarrealA = float(input("Digite o valor que você quer transformar em real: US$ "))
                    dolarreal = float(dolarrealA) * float(cotacao_dolar_para_real)
                    print(f"Você possui: R$ {dolarreal:.2f}")
                    time.sleep(0.5)
                    continuar()
                except ValueError:
                    print("Número inválido.")
                    time.sleep(1)
                    continue

        if moeda == 3:
            while True:
                try:
                    realeuroA = float(input("Digite o valor que você quer transformar em euro: R$ "))
                    realeuro = float(realeuroA) * float(cotacao_real_para_euro)
                    print(f"Você possui: EUR€ {realeuro:.2f}")
                    time.sleep(0.5)
                    continuar()
                except ValueError:
                    print("Número inválido.")
                    time.sleep(1)
                    continue

        if moeda == 4:
            while True:
                try:
                    eurorealA = float(input("Digite o valor que você quer transformar em real: EUR€ "))
                    euroreal = float(eurorealA) * float(cotacao_euro_para_real)
                    print(f"Você possui: R$ {euroreal:.2f}")
                    time.sleep(0.5)
                    continuar()
                except ValueError:
                    print("Número inválido.")
                    time.sleep(1)
                    continue

        if moeda == 5:
            while True:
                try:
                    dolareuroA = float(input("Digite o valor que você quer transformar em euro: US$ "))
                    dolareuro = (float(dolareuroA) * (float(cotacao_dolar_para_euro)))
                    print(f"Você possui: EUR€ {dolareuro:.2f}")
                    time.sleep(0.5)
                    continuar()
                except ValueError:
                    print("Número inválido.")
                    time.sleep(1)
                    continue

        if moeda == 6:
            while True:
                try:
                    eurodolarA = float(input("Digite o valor que você quer transformar em dólar: EUR€ "))
                    eurodolar = float(eurodolarA) * float(cotacao_euro_para_dolar)
                    print(f"Você possui: U$ {eurodolar:.2f}")
                    time.sleep(0.5)
                    continuar()
                except ValueError:
                    print("Número inválido.")
                    time.sleep(1)
                    continue
        if moeda == 7:
            sair()

main() 

