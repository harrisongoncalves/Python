mediaum = float(input("Olá, vamos tirar a sua média escolar e veremos se você foi aprovado ou não. Primeiramente, digite a sua média do 1º bimestre: "))
while mediaum < 0 or mediaum > 10:
    mediaum = float(input("Número fora dos limite. Digite novamente sua nota do 1º bimestre: "))
mediadois = float(input("Agora, sua nota do 2º bimestre: "))
while mediadois < 0 or mediadois > 10:
    mediadois = float(input("Número fora dos limite. Digite novamente sua nota do 2º bimestre: "))
mediatres = float(input("Agora, sua nota do 3º bimestre: "))
while mediatres < 0 or mediatres > 10:
    mediatres = float(input("Número fora dos limite. Digite novamente sua nota do 3º bimestre: "))
mediaquatro= float(input("Agora, sua nota do 4º bimestre: "))
while mediaquatro < 0 or mediaquatro > 10:
    mediaquatro = float(input("Número fora dos limite. Digite novamente sua nota do 4º bimestre: "))
media = float(round(mediaum + mediadois + mediatres + mediaquatro)) / 4
if media >= 6.0:
    print(f"Sua média anual foi {media}. Você passou de ano.")
else:
    print(f"Sua média anual foi {media}, o que é menor que a média exigida. Ou seja, você foi reprovado(a).")