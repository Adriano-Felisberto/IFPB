contador = 0

while True:
        
        contador += 1
        print(f"{contador} tentativa")

        num = int(input(f"digite o número {contador}: "))

        if contador == 5:
            print("Você perdeu o jogo")
            break

        if num > 50:
            print(f"o número {num} é maior que 50")
            break

        elif num < 50:
            print(f"o número {num} é menor que 50")
            print("Tente novamente")
            
        else:
            print("Parabéns você acertou o número")
            break
