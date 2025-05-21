"""Escreva um programa que leia uma temperatura em graus Celsius e a apresente
convertida em graus Fahrenheit. A fórmula de conversão é: F = (9*C+160) / 5,
sendo F a temperatura em Fahrenheit, e C a temperatura em Celsius."""

celsius = float(input("Digite quantos graus celsius: C°"))

print(f"{celsius:.2}°C para Fahrenheit é igual {(9 * celsius + 160) / 5}°F")