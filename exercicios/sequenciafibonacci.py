def seqfibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    else:
        return False
def main():
    while True:
        try:
            numero = int(input("Digite um número: "))
            if seqfibonacci(numero):
                print(f"O número: {numero} pertence.")
            else:
                print(f"O número: {numero} não pertence.")
        except ValueError:
            print("Digite um número válido.")
main()