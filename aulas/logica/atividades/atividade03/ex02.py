"""Faça um programa que peça um valor e mostre na tela se o valor é positivo ou
negativo."""

num = int(input("Digite um número: "))

if num > 0:
    print("O número informado e positivo.")
elif num < 0:
    print("O número informado é negativo")
else:
    print("O número é neutro")