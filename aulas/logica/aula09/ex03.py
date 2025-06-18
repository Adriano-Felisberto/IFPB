li = int(input("Limite inferior: "))
ls = int(input("Limite superior: "))
soma = 0
for x in range(li, ls ):
    if x % 2 == 0:
        print(x)
        soma += x
print(f"soma: {soma}")
