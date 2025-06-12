"""A sequência de Fibonacci é uma famosa sequência de números determinada
pela seguinte lei de formação:
○ Os dois primeiros termos da sequência são os números 0 e 1;
○ Do terceiro termo em diante, cada um é determinado pela soma dos dois
anteriores.

Veja: 0+1=1, 1+1=2, 2+1=3, 3+2=5 e assim sucessivamente. Assim, o início da
sequência é: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...). Sabendo disso, escreva um
programa em Python que lê do usuário um valor N e retorna uma lista contendo
os N primeiros termos da sequência de Fibonacci."""


n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))


fibonacci = []

for i in range(n):
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print("Sequência de Fibonacci:")
print(fibonacci)
