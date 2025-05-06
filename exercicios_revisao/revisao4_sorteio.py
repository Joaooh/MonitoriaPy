# Crie um programa de sorteio. O usuário digitará 5 números de 1 a 50.
# Em seguida, 5 números serão sorteados, mostre os acertos.

import random

num_usuario = []
contador = 0
while contador < 5:
    numero = int(input("Digite um número (1 a 50): "))
    num_usuario.append(numero)
    contador += 1

aleatorio = random.sample(range(1, 51), 5)

conj_numero = set(num_usuario)
conj_aleatorio = set(aleatorio)
acertos = conj_numero & conj_aleatorio

if acertos:
    print(f"\nVocê acertou {len(acertos)} número(s): {acertos}")
else:
    print("\nVocê acertou 0 números")
print(f"Números gerados: {conj_aleatorio}")