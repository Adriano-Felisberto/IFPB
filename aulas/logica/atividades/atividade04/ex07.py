"""Faça um programa que leia a quantidade de pessoas de um grupo e para cada
uma delas leia o nome e a altura. No final exiba: o nome e a altura da menor
pessoa do grupo; a altura média do grupo e o número de pessoas com altura
maior que 1.85 metros."""

npessoas = int(input("Digite a quantidade de pessoas: "))
for i in range(0, npessoas, +1):
    nome = str(input(f"digite o nome da pessoa {i+1}:"))
    altura = float(input(f"digite a altura da pessoa {i+1}:"))
    if i == 0:
        menor = altura
        nomeM = nome
    else:
        if altura < menor:
            menor = altura
            nomeM = nome
        print(f"O nome da pessoa mais baixa é: {nomeM} e a altura é: {menor}")