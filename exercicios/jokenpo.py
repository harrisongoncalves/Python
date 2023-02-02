class Jokenpo:
    pass

import random
import time

def brincadeira():
    jokenpo = ['pedra', 'papel', 'tesoura']
    ia = random.choice(jokenpo)
    print("Bem vindo a brincadeira do 'Pedra, Papel e Tesoura'.\n")
    escolha = input("Para começar, digite sua escolha (Pedra, Papel, Tesoura ou Sair): ").lower()
    if escolha == ia:
        print(f"Você escolheu {escolha} e o computador também escolheu {ia}. Vocês empataram.\n")
    elif escolha == 'pedra' and ia == 'tesoura':
        print(f"O computador escolheu {ia} e você escolheu {escolha}. Ou seja, Você venceu!!\n")
    elif escolha == 'tesoura' and ia == 'papel':
        print(f"O computador escolheu {ia} e você escolheu {escolha}. Ou seja, Você venceu!!\n")
    elif escolha == 'papel' and ia == 'pedra':
        print(f"O computador escolheu {ia} e você escolheu {escolha}. Ou seja, Você venceu!!\n")
    elif escolha == 'pedra' and ia == 'papel' or escolha == 'papel' and ia == 'tesoura' or escolha == 'tesoura' and ia == 'pedra':
        print(f"O computador escolheu {ia} e você escolheu {escolha}. Ou seja, você perdeu =(\n")
    elif escolha == 'sair':
        print("Obrigado por utilizar meu programa.")
        time.sleep(0.75)
        exit()
    else:
        print("Você precisa selecionar uma opção entre: Pedra, Papel e Tesoura.\n")
    brincadeira()

brincadeira()

