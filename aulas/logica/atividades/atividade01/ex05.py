"""Escreva um programa que efetue a apresentação do valor da conversão em real
(R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar ao usuário o
valor da cotação do dólar, e também a quantidade de dólares que ele deseja
converter."""

cotacao = float(input("Digite o valor da cotação do dolar: US$"))

dolar = float(input("Digite o valor de dolar para a converção: US$"))

conversao = dolar * cotacao

print(f"O valor em reais é de {conversao:.2}")