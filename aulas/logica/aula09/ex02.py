soma = 0
contador = 0

while True:
    num = int(input("Digite um número inteiro(0 para sair): "))
    if num == 0:
        break
    soma += num
    contador += 1
if contador == 0:
    print("Nenhum número foi inserido")
else:
    media = soma / contador
    print(f"A média aritmética dos números digitados é: {media:.2f}")