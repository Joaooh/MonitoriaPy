def linhas():
    print("-" * 28)

linhas()
print("Verificador de Palíndromo".center(28))
linhas()

lista = []
palavra = str(input("Digite uma palavra: ").lower())
ultimaLetra = len(palavra) - 1 

for i in range(ultimaLetra, -1, -1):
    lista.append(palavra[i])
contrario = "".join(lista)

if palavra == contrario:
    linhas()
    print(f"O contrário de '{palavra}' é '{contrario}'.")
    print("É um palíndromo!\n")
else:
    linhas()
    print(f"O contrário de '{palavra}' é '{contrario}'.")
    print("Não é um palíndromo!\n")