"""Faça um programa que pergunte em que turno você estuda. Peça para digitar M
(matutino), V (vespertino) ou N (noturno). Imprima a mensagem “Bom Dia!”, “Boa
Tarde!” ou “Boa Noite!” ou “Valor Inválido!”, conforme o caso."""

estacivi = input("""Digite uma das seguintes letras: 
M - matutino
V - vespetino
N - noturno
""").upper()

if estacivi == "M":
    print("Bom dia!")

elif estacivi == "V":
    print("Boa Tarde!")

elif estacivi == "N":
    print("Boa noite!")
else:
    print("Valor inválido")
