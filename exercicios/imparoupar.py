import random
import time


def main():
    while True:
        suaescolha = input("Escolha par ou ímpar: ").lower()
        if suaescolha != "par" and suaescolha != "ímpar":
            print("Escolha inválida, escolha par ou ímpar")
            time.sleep(1)
            continue

        seunumero = int(input("Escolha um número de 0 a 10: "))
        if seunumero < 0 or seunumero > 10:
            print("Número inválido, escolha um número de 0 a 10.")
            time.sleep(1)
            continue

        pcnumero = random.randint(1, 10)

        if suaescolha == "par":
            print(f"Como você escolheu par, a máquina escolheu ímpar. O número que a máquina escolheu foi {pcnumero}.")
        else:
            print(f"Como você escolheu ímpar, a máquina escolheu par. O número que a máquina escolheu foi {pcnumero}.")
        
        total = pcnumero + seunumero
        if total % 2 == 0:
            resultado = "par"
        else:
            resultado = "ímpar"
            
        time.sleep(0.5)
        print(f"{seunumero} + {pcnumero} = {total} ({resultado})")

        if resultado == suaescolha:
            time.sleep(0.25)
            print("Parabéns, você ganhou!!")
        else:
            time.sleep(0.25)
            print("Infelizmente, você perdeu. =(")

        time.sleep(0.5)
        jogarnovamente = input("Jogar novamente? (s/n): ")
        if jogarnovamente == 'n':
            exit()

main()
             


