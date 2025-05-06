# Crie uma função que recebe um número e informa se é um número primo.

numero = int(input("Digite um número: "))

if numero > 1:
    contador = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            contador += 1
    if contador == 2:
        print(f"{numero} é um número primo!")
    else:
        print(f"{numero} não é um número primo.")
else:
    print("Números menores ou iguais a 1 não são primos")