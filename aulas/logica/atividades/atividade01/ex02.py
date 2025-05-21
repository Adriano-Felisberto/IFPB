"""Faça um programa que peça dois números naturais ao usuário e imprima a  
divisão do primeiro número pelo segundo. Avise ao usuário que o segundo  número não pode ser 0. """

numn1 = int(input("Digite um número natural: "))
numn2 = int(input("Digite outro número natural: "))

if numn1 == 0 or numn2 == 0:
    print("Erro: nenhum dos dois números pode ser 0.")
else:
    calculo = numn1 / numn2
    print(f"A divisão de {numn1} por {numn2} é {calculo}")
