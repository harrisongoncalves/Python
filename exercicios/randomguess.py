class RandomGuess:
    pass

import random as r

## Exercício que eu vi no Google.

def guess(x):
    numero_aleatorio = r.randint(1, x)
    guess = 0
    while guess != numero_aleatorio:
        guess = int(input(f"Adivinhe o número, entre 1 e {x}: "))
        if guess < numero_aleatorio:
            print("Desculpe, adivinhe novamente. O número que você digitou é muito baixo: ")
        elif guess > x:
            print("Número maior que o permitido, tente novamente: ")
        elif guess > numero_aleatorio:
            print("Desculpe, adivinhe novamente. O número que você digitou é muito alto: ")
        
    print("Parabéns, você acertou o número. =)")

guess(10)
