## Meu primeiro projeto Python.


seunome = str(input("Olá, primeiramente, digite seu nome: "))
seunome = seunome.capitalize()
seunome = seunome.strip()
seunome = seunome.split(None, 1)[0] ## pega apenas primeiro nome


print(f"Olá, {seunome}. Este é o checador de pedofilia. Checaremos se você ou a pessoa que você quer se relacionar/já se relaciona é pedófilo(a).")
suaidade = int(input("Me informe a sua idade: "))
while True:
    try:
        suaidade = int(input("Me informe a sua idade: "))
        idadedele = int(input("Agora informe a idade da outra pessoa: "))
    except ValueError:
            print("Não é permitido utilizar caracteres, apenas números.")
    else:
        break
if suaidade >= 18 and idadedele <= 14:
    print("Você será pedófilo(a) caso se relacione com essa pessoa.")
elif suaidade <= 14 and idadedele >= 18:
    print("Será pedofilia da parte da outra pessoa, não se relacione com ela.")
elif suaidade >= 15 and suaidade <= 17 and idadedele >= 11 and idadedele <= 13:
    print("Perante a lei não é pedofilia, mas é bem estranho. As pessoas vão olhar com estranheza esta relação.")
elif suaidade >= 18 and idadedele >= 18:
    print ("Não é pedofilia")



