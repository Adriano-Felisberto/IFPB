"""Crie um programa em Python que solicite ao usuário para digitar um número (n).
Em seguida, ler n números da entrada e imprimir o triplo de cada um."""

n = int(input("digite um número: "))

for i in range(0, n):
    print(f"{i} x 3 = {i * 3}")