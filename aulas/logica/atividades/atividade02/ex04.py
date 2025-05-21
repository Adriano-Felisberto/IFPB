"""Agora, faça um programa em Python, que mostra o resultado do AND na tela
para todas as combinações de valores vistas na questão anterior. A impressão
será no formato: “O resultado da operação True and True é “ e o valor da
resposta."""

valores = [(False, False), (False, True), (True, False), (True, True)]

print(f"{'Valor 1':^10} | {'Valor 2':^10} | {'Resultado do AND':^20}")
print("-" * 45)

for v1, v2 in valores:
    resultado = v1 and v2
    print(f"{str(v1):^10} | {str(v2):^10} | {str(resultado):^20}")
