"""Crie um programa em Python que solicite um número ao usuário e que, logo em
seguida, imprima a tabuada de multiplicação desse número."""

n = int(input("Digite um número: "))
for i in range(0, 11):
    print(f"{n} x {i} = {n * i}")
