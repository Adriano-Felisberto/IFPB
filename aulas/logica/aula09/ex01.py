"""Faça um programa que leia números inteiros e no final seja
informado quantos números estão no intervalo entre 25 (incluso)
e 50 (não incluso). A leitura de um número negativo indica o fim
da leitura dos números."""

contador = 0

while True:
    num = int(input("Digite um número inteiro: "))
    if num < 0:
        break
    if num >= 25 and num < 50:
        contador +=  1

print(f"Quantidade de números no intervalo entre 25 e 50: {contador}")