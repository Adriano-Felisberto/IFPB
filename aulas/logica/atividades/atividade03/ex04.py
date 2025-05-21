"""Faça um programa que verifique se uma letra digitada é “C”, “S” ou “D”.
Conforme a letra, escrever: C - Casado, S - Solteiro, D - Divorciado, Estado Civil
Inválido (para qualquer outra letra digitada)."""

estacivi = input("""Digite uma das seguintes letras: 
C - casado
S - solteiro
D - divorciado
""").upper()

if estacivi == "C":
    print("Seu estado civil atual é casado")

elif estacivi == "D":
    print("Seu estado civil atual é divorciado")

elif estacivi == "S":
    print("Seu estado civil atual é solteiro")
else:
    print("inválido")
