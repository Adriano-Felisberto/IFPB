"""Uma empresa quer dar um bônus de Natal (em dezembro, claro) para seus
empregados que será 60% do cálculo médio do salário de trabalho.
Considerando que todos na empresa ganhem um mesmo valor de salário,
elabore um programa que receba a entrada do salário e imprima o valor do bônus
de Natal e o valor a ser depositado na conta de cada empregado em dezembro."""

salario = float(input("Digite o sálario dos empregados da empresa: R$"))

bonus = (salario * 60) / 100

bonus_dezembro = salario + bonus

print(f"O sálario antes do bonus era de R${salario} agora pós o bonus virou R${bonus_dezembro}")