"""Faça um programa que peça um valor e mostre na tela se o valor é positivo ou
negativo."""

num = int(input("Digite um númmero: "))

if num % 2 == 0:
    print(f"O número {num} é par")

elif num % 2 != 0:
    print(f"O número {num} é impar")
