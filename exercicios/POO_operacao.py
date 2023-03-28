

class Operacao:
    def operacao(self, n1, n2, sinal):
        sinal = sinal.strip()
        sinal = sinal.lower()
        if sinal == "+" or sinal == "soma":
            resultado = n1 + n2
            return resultado
        elif sinal == "-" or sinal == "subtracao":
            resultado = n1 - n2
            return resultado
        elif sinal == "*" or sinal == "multiplicacao":
            resultado = (n1 * n2)
            return resultado
        elif sinal == "/" or sinal == "divisao":
            resultado = n1 / n2
            return resultado
        else:
            return ("Opção inválida!")

    
