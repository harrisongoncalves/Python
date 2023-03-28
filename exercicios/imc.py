import time
def continuar():
    while True: 
        novamente = input("Deseja realizar outro cálculo de IMC? (s/n): ")
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


print("Calculadora de IMC\n")

def main():
    while True:
        try:      
            peso = float(input("Digite o seu peso: ").replace(",", "."))
            while True:
                try:
                    altura = float(input("Agora, a sua altura em metros: ").replace(",", "."))
                except ValueError:
                    print("Por favor, digite um número válido.")
                    continue    
                imc = peso / (altura ** 2)
                if imc < 18.5:
                    print(f"Seu IMC é: {imc:.2f}. E sua classificação é magreza.")
                    continuar()
                elif imc >= 18.5 and imc <= 24.9:
                    print(f"Seu IMC é: {imc:.2f}. E sua classificação é normal.")
                    continuar()
                elif imc >= 25 and imc <= 29.9:
                    print(f"Seu IMC é: {imc:.2f}. E sua classificação é sobrepeso.")
                    continuar()
                elif imc >= 30 and imc <= 39.9:
                    print(f"Seu IMC é: {imc:.2f}. E sua classificação é obesidade.")
                    continuar()
                elif imc >= 40:
                    print(f"Seu IMC é: {imc:.2f}. E sua classificação é obesidade grave.")
                    continuar()
        except ValueError:
                print("Por favor, digite um número válido.")
                continue   
main() 
        