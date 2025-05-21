"""Faça um programa que solicite ao usuário dois números e mostre todos os
resultados de possíveis de operações relacionais entre eles, ou seja, deve
mostrar todos os resultados das operações iniciando com um número e depois
com outro. Por exemplo:
○ Usuário informa 6 e 8
a) Então, por exemplo, o programa deve imprimir os resultados de
6 > 8 e 6 < 8, e repetindo essa mesma lógica para todas as
outras operações relacionais existentes;
b) Os resultados devem ser impressos no seguinte formato: “O
valor da avaliação da expressão 6 > 8 é False”.
"""

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print(f"Resultados de {a} em relação a {b}:")
print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}")
print(f"{a} > {b}  = {a > b}")
print(f"{a} < {b}  = {a < b}")
print(f"{a} >= {b} = {a >= b}")
print(f"{a} <= {b} = {a <= b}")

print(f"\nResultados de {b} em relação a {a}:")
print(f"{b} == {a} = {b == a}")
print(f"{b} != {a} = {b != a}")
print(f"{b} > {a}  = {b > a}")
print(f"{b} < {a}  = {b < a}")
print(f"{b} >= {a} = {b >= a}")
print(f"{b} <= {a} = {b <= a}")
