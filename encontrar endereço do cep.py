import requests
import json
import time

def main():
    while True:
        cep = (input("Digite aqui o CEP que você quer procurar: "))
        cep = int(cep.replace('-', ''))
        link = f"https://viacep.com.br/ws/{cep}/json/"
        apicep = requests.get(link)
        apicep = apicep.json()
        logradouro = str(apicep['logradouro'])
        bairro = str(apicep['bairro'])
        cidade = str(apicep['localidade'])
        print(f"O endereço é: {logradouro}. A rua está localizada no bairro de {bairro}, na cidade de {cidade}.")
        time.sleep(0.5)
            
        novamente = input("Quer pesquisar outro cep? (s/n): ")
        if novamente == 'n':
            exit()
        
main()

