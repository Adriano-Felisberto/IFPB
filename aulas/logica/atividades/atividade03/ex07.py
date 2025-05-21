"""Faça um programa que leia 3 números e calcule a média ponderada entre eles.
Considere que o maior número recebe peso 5 e os outros dois recebem peso
2,5."""

num = int(input("Digite um número: "))
num2 = int(input("Digite um outro número: "))
num3 = int(input("Digite um outro número: "))

lista = [num, num2, num3]

maior = max(lista)

if num == maior:
    peso1 = 5
else:
    peso1 = 2.5

if num2 == maior:
    peso2 = 5
else:
    peso2 = 2.5

if num3 == maior:
    peso3 = 5
else:
    peso3 = 2.5

soma_pesos = peso1 + peso2 + peso3
media_ponderada = (num * peso1 + num2 * peso2 + num3 * peso3) / soma_pesos

# Mostra o resultado
print(f"A média ponderada é: {media_ponderada:.2f}")
