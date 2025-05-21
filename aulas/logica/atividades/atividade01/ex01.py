"""Faça um programa que peça um número natural ao usuário e imprima o  quadrado desse número. 
"""
while True:
    numero = int(input("Digite um número: "))
    print(f"O {numero} ao quadrado é {numero * 2}")
    while True:
        esco = int(input("Digite se você deseja continuar: [1]Sim [2] Não"))
        if esco == 1:
            print("Carregando novamente...")
        if esco == 2:
            print("Programa encerrado...")
            break
        else:
            print("Opção inválida. Tente novamente.")