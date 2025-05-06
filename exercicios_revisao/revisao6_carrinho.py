# Crie um menu que simula um carrinho de mercado on-line.
# Permita a visualização do carrinho, adicionar ou remover um item ou sua quantidade específica.

def linhas():
    print("-" * 54)

def mostrar_carrinho():
    print()
    linhas()
    print("Carrinho atual:")
    if carrinho:
        for produto in sorted(carrinho):
            print(f"{produto}: {carrinho[produto]}")
    else:
        print("O carrinho está vazio.")
    linhas()

carrinho = {
    "arroz": 2,
    "feijão": 3,
    "detergente": 6,
    "suco": 5
}

linhas()
print("Carrinho inicial:\n")
for produto in sorted(carrinho):
    print(f"{produto}: {carrinho[produto]}")
linhas()

while True:
    print("1 - Adicionar novo item")
    print("2 - Remover um item")
    print("3 - Atualizar quantidade de um item")
    print("4 - Visualizar carrinho")
    print("5 - Sair")

    escolha = input("O que gostaria de fazer? ")

    match escolha:
        # Adicionar novo item
        case '1':
            novo_item = input("\nNome do novo item: ").strip().lower()
            if novo_item in carrinho:
                print(f"O produto '{novo_item}' já está no carrinho.")
            else:
                try:
                    quant = int(input("Quantidade: "))
                    if quant > 0:
                        carrinho[novo_item] = quant
                        print(f"Produto '{novo_item}' adicionado! Qtde: {quant}.")
                    else:
                        print("A quantidade deve ser maior que zero.")
                except ValueError:
                    print("Por favor, insira um número válido.")
            mostrar_carrinho()
        # Remover um item
        case '2':
            remover_item = input("\nNome do item a remover: ").strip().lower()
            if remover_item not in carrinho:
                print(f"O produto '{remover_item}' não está no carrinho.")
            else:
                quantidade_atual = carrinho[remover_item]
                if quantidade_atual > 1:
                    try:
                        remover_quant = int(input(f"Quantidade a remover (no carrinho: {quantidade_atual}): "))
                        if remover_quant <= 0:
                            print("A quantidade deve ser maior que zero.")
                        elif remover_quant >= quantidade_atual:
                            del carrinho[remover_item]
                            print(f"Produto '{remover_item}' removido do carrinho.")
                        else:
                            carrinho[remover_item] -= remover_quant
                            print(f"{remover_quant} unidade(s) de '{remover_item}' removida(s).")
                    except ValueError:
                        print("Por favor, insira um número válido.")
                else:
                    del carrinho[remover_item]
                    print(f"Produto '{remover_item}' removido do carrinho.")
            mostrar_carrinho()
        # Atualizar quantidade de um item
        case '3':
            item = input("\nQual item deseja atualizar? ").strip().lower()
            if item not in carrinho:
                print(f"O produto '{item}' não está no carrinho.")
            else:
                try:
                    nova_quant = int(input("Nova quantidade: "))
                    if nova_quant > 0:
                        carrinho[item] = nova_quant
                        print(f"Quantidade de '{item}' atualizada para {nova_quant}.")
                    else:
                        del carrinho[item]
                        print(f"Produto '{item}' removido do carrinho (quantidade zerada).")
                except ValueError:
                    print("Por favor, insira um número válido.")
            mostrar_carrinho()
        # Visualizar carrinho
        case '4':
            mostrar_carrinho()
        # Sair
        case '5':
            print("Finalizando...\n")
            break
        # Se o usuário escolher uma opção inexistente
        case _:
            print("\nOpção inválida. Tente novamente.")
            linhas()