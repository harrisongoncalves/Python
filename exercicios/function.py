produtos = ["ABC123", "abd012", " ABS111", "abB222"]

def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto

for i, produto in enumerate(produtos):
    produtos[i] = tratar_texto(produto)
    
print(produtos)

## transformar int em string

numeros = [67, 79585, 79585, 3, -1]

def number_to_string(numb):
    numb = str(numb)
    return numb

for i, numero in enumerate(numeros):
    numeros[i] = number_to_string(numero)

print(numeros)


##

def even_or_odd(number):
    if (number % 2 == 0):
        print(f"O número {number} é Even")
    else:
        print(f"O número {number} é Odd")
    return 

numeros = [2, 1, 0, 1545452, 7, 78, 17, 74156741, 100000, -123, -456]

for numero in range(1,11):
    numero = even_or_odd(numero)

print(numero)

