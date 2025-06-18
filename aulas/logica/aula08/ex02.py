for i in range(0, 10, +1):
    num = int(input(f"digite um número:"))
    if i == 0:
        menor = num
        maior = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num

print(f"O menor número é {menor} e o maior número é {maior}")