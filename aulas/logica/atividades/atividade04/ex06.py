"""Crie um algoritmo em Pyhton que solicite ao usuário um número de entrada (n),
leia n números inteiros da entrada e imprima o maior deles. Suponha que todos
os números lidos serão positivos."""

n = int(input("Digiteo número de vezes: "))
maior = 0
for i in range(0, n, +1):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
print(f"O maior número é: {maior}")