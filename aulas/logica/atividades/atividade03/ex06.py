""""Faça um programa que leia 3 valores e escreva o produto dos 2 maiores."""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 <= num2 and num1 <= num3:
    produto = num2 * num3

elif num2 <= num1 and num2 <= num3:
    produto = num1 * num3

else:
    produto = num1 * num2

print(f"O produto dos dois maiores números é: {produto}")

