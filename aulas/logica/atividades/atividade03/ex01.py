"""Faça um programa que peça dois números e imprima o maior deles."""

num = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num > num2:
    print(f"O número {num} é maior que {num2}")
elif num2 > num:
    print(f"O número {num2} é maior que {num}")
else:
    print(f"Nenhum dos números informados é maior que o outro")