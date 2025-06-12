"""Crie um programa em python que solicite ao usuário para digitar o nome e o
salário bruto de 10 pessoas. Para cada nome e salário bruto digitado, logo em
seguida deve ser impresso o nome e o valor líquido do seu salário considerando
a porcentagem de alíquota do imposto de renda, conforme abaixo:
○ salário menor que R$2.200,00: isento
○ salário > = R$2.200,00 e < R$2.800,00: 7,5% do salário bruto
○ salário >= R$ 2.800,00 e < R$3.700,00: 15% do salário bruto
○ salário >= R$3.700,00: 22,5% do salário bruto"""

for i in range(0, 10, +1):
    nome = str(input(f"digite o nome da pessoa {i+1}:"))
    salario = float(input(f"Digite o seu salario bruto da pessoa {i+1}:"))
    if salario < 2200:
        print(f"O salario de {nome} é isento")
    elif salario >= 2200 and salario < 2800:
        print(f"O salario de {nome} é de 7,5% do salario bruto")
    elif salario >= 2800 and salario < 3700:
        print(f"O salario de {nome} é de 15% do salario bruto")
    else:
        print(f"O salario de {nome} é de 22,5% do salario bruto")