def linhas():
    print("-" * 28)

def contador(lista):
    contagem = {}
    for numero in lista:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1
    return contagem

linhas()
print("Contador de Elementos".center(28))
print("Digite 0 para sair".center(28))
linhas()

lista = []
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    else:
        lista.append(numero)
resultado = contador(lista)
linhas()
print(f"{resultado}\n")