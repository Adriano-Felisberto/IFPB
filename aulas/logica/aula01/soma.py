while True:
    operação = int(input("""ESCOLHA ENTRE AS 4 OPERAÇÕES
                        [1]SOMA, [2]SUBTRAÇÃO, [3] MULTIPLICAÇÃO, [4] DIVISÃO
                        SUA ESCOLHA: """))
    n1 = float(input("DIGITE UM NUMERO: "))
    n2 = float(input("DIGITE OUTRO NUMERO: "))
    if operação == 1:
        CALCULO = n1 + n2
        print(CALCULO)
        
    elif operação ==2:
        CALCULO = n1 - n2
        print(CALCULO)
    elif operação == 3:
        CALCULO = n1 * n2
        print(CALCULO)
    elif operação == 4:
        CALCULO = n1 / n2
        print(CALCULO)
    ESCO = int(input("você quer fazer um novo calculo? [1]sim ou [2]não"))
    if ESCO == 1:
        print("Vamos lá")
    elif ESCO == 2:
        print("PROGRAMA ENCERRADO...")
        break
    else:
        print("ESCOLHA NOVAMENTE DADO ERRADO")