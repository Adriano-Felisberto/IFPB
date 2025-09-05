import time
frutas = []
for i in range(10):
    while True:
        novafruta = input(f"Digite o nome da fruta {i+1}: ").strip()
        if novafruta in frutas:
            print("Essa fruta já foi adicionada! Digite outra.")
        else:
            frutas.append(novafruta)
            break

while True:
    print("""menu:
          1- pesqusar fruta
          2- remover fruta
          0- encerrar programa """)
    solicitação = int(input("escolha uma opção: "))
    if solicitação == 1:
        pesquisa = input("digite o nome de uma fruta para a pesquisa: ")
        if pesquisa in frutas:
            print(f"A fruta {pesquisa} está na lista")
        else:
            print("Não se encontra na lista")
    elif solicitação == 2:
        pesquisa = input("digite o nome de uma fruta para a pesquisa: ")
        if pesquisa in frutas:
            print(f"A fruta {pesquisa} está na lista")
            print("preparando ação de remoção...")
            for i in range(3, 0, -1):
                print(i)
                time.sleep(1)
            frutas.remove(pesquisa)
            print("nova lista")
            print(frutas)
        else:
            print("Não se encontra na lista")
    elif solicitação == 0:
        print("programa encerrado...")
        break
    else:
        print("opção invalida tente novamente")