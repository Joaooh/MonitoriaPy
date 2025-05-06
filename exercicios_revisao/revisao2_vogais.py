# Faça um programa que receba uma palavra e descubra quantas vogais existem na palavra.

palavra = str(input("Digite uma palavra: ").lower())
vogais = "aeiou"
ct = 0
for letra in palavra:
    if letra in vogais:
        ct +=  1
print(ct)