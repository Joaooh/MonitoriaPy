# Exercícios - Monitoria de Python

Este repositório reúne exercícios classificados como de dificuldade Difícil, resolvidos durante a monitoria de Python da faculdade. Cada exercício propõe a criação de scripts que trabalham com lógica de programação, estruturas de controle, tipos de dados e outros conceitos fundamentais da linguagem.

## Índice

- [Exercício 1: Classificador de Título de Jogador](#exercício-1-classificador-de-título-de-jogador)
- [Exercício 2: Verificador de Palíndromos](#exercício-2-verificador-de-palíndromos)
- [Exercício 3: Contador de Elementos em Lista](#exercício-3-contador-de-elementos-em-lista)

---

## Exercício 1: Classificador de Título de Jogador

**Arquivo:** `exerc1-jogo.py`

Este exercício propõe a criação de um pequeno sistema de RPG que determina o título de um jogador com base na sua classe, nível e posse de item especial. Parte da aula 2.

### Regras

- Perguntas ao usuário:
  - Classe: `Guerreiro` ou `Ladino`
  - Nível: número inteiro ≥ 0
  - Possui item especial? (`sim` ou `não`)
- O título depende das respostas, conforme a tabela:

| Classe   | Nível   | Item especial | Título            |
|----------|---------|----------------|-------------------|
| Guerreiro| ≥ 30    | Sim            | Guerreiro Maior   |
| Guerreiro| < 30    | Sim            | Guerreiro Menor   |
| Ladino   | ≥ 30    | Sim            | Ladino Maior      |
| Ladino   | < 30    | Sim            | Ladino Menor      |

### Exemplo

```plaintext
Qual a sua classe?
Opções: Guerreiro, Ladino: guerreiro

Qual o seu nível? 32

Você tem um item especial? (S/N): s

Título: Guerreiro Maior.
```

### Aprendizados

- Estruturas de repetição e validação de dados (`while`, `try/except`)
- Uso de condicionais (`if`, `elif`, `else`)
- Conversão de strings para outros tipos (`int`, `bool`)
- Tratamento de entrada de dados do usuário

---

## Exercício 2: Verificador de Palíndromos

**Arquivo:** `exerc2-palindromo.py`

Este exercício propõe a criação de um verificador de palíndromos. O programa recebe uma palavra do usuário, inverte essa palavra utilizando uma lista (ao invés do fatiamento direto com `[::-1]`) e informa se ela é ou não um palíndromo. Parte da aula 3.

### Regras

- Criar uma função que receba uma string como parâmetro
- Verificar se a string é um palíndromo (ou seja, se ela se mantém igual de trás para frente)
- Mostrar na tela se a palavra é ou não um palíndromo

### Exemplos

```plaintext
Digite uma palavra: ovo

O contrário de 'ovo' é 'ovo'.
É um palíndromo!
```

```plaintext
Digite uma palavra: banana

O contrário de 'banana' é 'ananab'.
Não é um palíndromo!
```

### Aprendizados

- Manipulação de strings
- Criação de listas dinâmicas
- Comparações lógicas
- Alternativa ao uso de fatiamento com `[::-1]`

---

## Exercício 3: Contador de Elementos em Lista

**Arquivo:** `exerc3-contador.py`

Neste exercício, o objetivo é criar uma função que recebe uma lista como entrada e retorna um dicionário com a contagem de quantas vezes cada elemento aparece, finalizando ao inserir 0 como valor. Parte da aula 3.

### Regras

- Criar uma função que receba uma lista
- Contar e mostrar quantas vezes cada elemento aparece na lista
- Exibir o resultado no formato de dicionário `{elemento: quantidade}`

### Exemplo

```plaintext
Digite um número: 1
Digite um número: 2
Digite um número: 2
Digite um número: 4
Digite um número: 4
Digite um número: 4
Digite um número: 0
{1: 1, 2: 2, 4: 3}
```

### Aprendizados

- Manipulação de listas
- Uso de dicionários para contagem
- Funções definidas pelo usuário
- Laços de repetição

---

## Como executar qualquer exercício:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Joaooh/MonitoriaPy.git
   cd MonitoriaPy
   ```

2. Execute o arquivo desejado:
   ```bash
   python exercX-nome.py
   ```
