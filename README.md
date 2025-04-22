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

Esta seção será atualizada posteriormente. Parte da aula 3.

---

## Exercício 3: Contador de Elementos em Lista


Esta seção será atualizada posteriormente. Parte da aula 3.

---

## Como executar qualquer exercício:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Joaooh/MonitoriaPy.git
   cd MonitoriaPy
   ```

2. Execute o arquivo desejado:
   ```bash
   python nome_do_arquivo.py
   ```
