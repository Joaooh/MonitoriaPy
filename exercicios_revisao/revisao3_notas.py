# Dado um dicionário de alunos com notas, exiba apenas os alunos com nota maior ou igual a 8.

dicionario = {
    "Ana": 8,
    "Bruno": 6,
    "Carlos": 4,
    "Diego": 9,
    "Eduarda": 3,
    "Fabrício": 7
}

for nome, nota in dicionario.items():
    if nota >= 8:
        print(f"Nome: {nome} | Nota: {nota}")