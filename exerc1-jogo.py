def linhas():
    print("-" * 40)

linhas()
print("Exercício Difícil - 5 pts".center(40))
linhas()

# Pergunta a classe do usuário, não aceitando valores diferentes de Guerreiro ou Ladino
classe = None
while classe not in ["guerreiro", "ladino"]:
    classe = str(input("Qual a sua classe?\nOpções: Guerreiro, Ladino: ")).lower().strip()
    if classe not in ["guerreiro", "ladino"]:
        print("Digite apenas Guerreiro ou Ladino.")

print("")

# Pergunta o nível do usuário, não aceitando valores menores que 0 e não inteiros
nivel = None
while nivel is None:
    try:
        nivel = int(input("Qual o seu nível? "))
        if nivel < 0:
            print("Seu nível não pode ser negativo.")
            nivel = None
    except ValueError:
        print("Digite um número inteiro válido.")

print("")

# Pergunta se tem item especial e continua perguntando até o usuário responder S ou N
item = None
while item not in ["s", "n"]:
    item = input("Você tem um item especial? (S/N): ").lower().strip()
    if item not in ["s", "n"]:
        print("Digite apenas S para sim ou N para não.")    

# Converte a resposta do usuário para um valor booleano
if item == "s":
    item = True
elif item == "n":
    item = False

# Define o título do usuário com base na classe, nível e item especial
if not item:
    titulo = "Sem título"
else:
    if classe == "guerreiro":
        titulo = "Guerreiro Menor" if nivel < 30 else "Guerreiro Maior"
    elif classe == "ladino":
        titulo = "Ladino menor" if nivel < 30 else "Ladino maior"

linhas()
print(f"Título: {titulo}.\n")