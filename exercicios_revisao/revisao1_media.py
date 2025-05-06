# Crie uma função que recebe uma lista de números e devolve a média deles.

def media(soma, quant):
    media = soma / quant
    return media

quant = int(input("Quantos números? "))
soma = 0
for i in range(1, quant+1):
    numero = int(input("Digite um número: "))
    soma += numero
print(f"Média: {media(soma, quant)}")