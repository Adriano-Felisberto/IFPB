"""while True:
    num = int(input('Digite um valor: '))
    if num <= 1:
        print(f'O fatorial de {num} é 1')
        break

    fatorial = 1
    while num > 1:
        fatorial = fatorial * num 
        num = num - 1

    print(f'O fatorial é {fatorial}')

"""

for i in range(16, 6, -2):
    if i % 2 == 0:
        print(i+1)
    elif i % 3 == 0:
        print(i-1)