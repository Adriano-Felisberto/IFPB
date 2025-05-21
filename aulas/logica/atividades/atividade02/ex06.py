"""Agora, faça um programa que receba os valores de x, y e z do usuário e mostre
o resultado da expressão da questão anterior.
"""
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))

w = x * y < z / x or x / y > z * x and z * y < x

print(f"O resultado da expressão é: {w}")
