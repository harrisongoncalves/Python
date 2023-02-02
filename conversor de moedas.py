import time
import math
import requests

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,EUR-USD,BRL-USD,USD-EUR,BRL-EUR")
cotacoes = cotacoes.json()

cotacao_dolar = float(cotacoes['USDBRL']["bid"])
cotacao_euro = float(cotacoes['EURBRL']["bid"])
cotacao_brlusd = float(cotacoes['BRLUSD']["bid"])
cotacao_brleur = float(cotacoes['BRLEUR']['bid'])
cotacao_eurodolar = float(cotacoes['EURUSD']["bid"])
cotacao_dolareuro = float(cotacoes['USDEUR']["bid"])

cotacaoDA = round(cotacao_dolar, 2)
cotacaoEA = round(cotacao_euro, 2)


def main():
    while True:
        print("Conversor de moedas")
        print(f"US$ = R$ {cotacaoDA} | EUR€ = R$ {cotacaoEA}\n")
        print("Selecione a opção de conversão:")
        print("1 --> Real para dólar\n"
        "2 --> Dólar para real\n"
        "3 --> Real para euro\n"
        "4 --> Euro para real\n"
        "5 --> Dólar para euro\n"
        "6 --> Euro para dólar\n"
        "7 --> Sair do programa")
        moeda = int(input("Digite a sua opção: "))
        if moeda < 1 and moeda > 7:
            print("Opção inválida, escolha entre 1 e 7.")
            time.sleep(2)
            continue
        
        if moeda == 1:
            realdolarA = float(input("Digite o valor que você quer transformar em dólar: R$ "))
            realdolar = float(realdolarA) * float(cotacao_brlusd)
            realdolarB = (round(realdolar, 2))
            print(f"Você possui: US$ {realdolarB}")
            time.sleep(0.5)
            novamente = input("Deseja realizar outra conversão? (s/n): ")
            if novamente== 'n':
                exit()

        if moeda == 2:
            dolarrealA = float(input("Digite o valor que você quer transformar em real: US$ "))
            dolarreal = float(dolarrealA) * float(cotacao_dolar)
            realdolarB = (round(dolarreal, 2))
            print(f"Você possui: R$ {realdolarB}")
            time.sleep(0.5)
            novamente = input("Deseja realizar outra conversão? (s/n): ")
            if novamente== 'n':
                exit()

        if moeda == 3:
            realeuroA = float(input("Digite o valor que você quer transformar em euro: R$ "))
            realeuro = float(realeuroA) * float(cotacao_brleur)
            realeuroB = (round(realeuro, 2))
            print(f"Você possui: EUR€ {realeuroB}")
            time.sleep(0.5)
            novamente = input("Deseja realizar outra conversão? (s/n): ")
            if novamente== 'n':
                exit()

        if moeda == 4:
            eurorealA = float(input("Digite o valor que você quer transformar em real: EUR€ "))
            euroreal = float(eurorealA) * float(cotacao_euro)
            eurorealB = (round(euroreal, 2))
            print(f"Você possui: R$ {eurorealB}")
            time.sleep(0.5)
            novamente = input("Deseja realizar outra conversão? (s/n): ")
            if novamente== 'n':
                exit()

        if moeda == 5:
            dolareuroA = float(input("Digite o valor que você quer transformar em euro: US$ "))
            dolareuro = (float(dolareuroA) * (float(cotacao_dolareuro)))
            dolareuroB = (round(dolareuro, 2))
            print(f"Você possui: EUR€ {dolareuroB}")
            time.sleep(0.5)
            novamente = input("Deseja realizar outra conversão? (s/n): ")
            if novamente== 'n':
                exit()

        if moeda == 6:
            eurodolarA = float(input("Digite o valor que você quer transformar em dólar: EUR€ "))
            eurodolar = float(eurodolarA) * float(cotacao_eurodolar)
            eurodolarB = round(eurodolar, 2)
            print(f"Você possui: U$ {eurodolarB}")
            time.sleep(0.5)
            novamente = input("Deseja realizar outra conversão? (s/n): ")
            if novamente== 'n':
                exit()

        if moeda == 7:
            print("Obrigado por utilizar o meu programa.")
            time.sleep(2)
            exit()

main() 

