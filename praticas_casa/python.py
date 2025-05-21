import random

while True:
    adi = int(input("Escolha um número de 1 a 20: "))
    compu = random.randint(1,20)
    if adi == compu:
        print("A partida deu empate o jogador escolheu {}, e computador escolheu {}".format(adi, compu))
    if adi > compu:
        print("A partida deu vitoria ao jogador escolheu {}, e o computador {}".format(adi, compu))
            
    
    if adi < compu:
        print("O resultado da partida foi que o computador ganhou, usando o número {} e o jogador {}".format(compu, adi))
        
    
    jogar = int(input("""Você quer jogar uma nova partida? 
            [1]sim [2]não
            sua resposta: """))
    if jogar == 1:
        print("Vamos a uma nova partida")
    if jogar == 2:
        print("Desligando o sistema...")
        break
            