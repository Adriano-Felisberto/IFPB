num = float(input("digite um numero: "))
num2 = int(input("digite o numero da potencia: "))
potencia = num ** num2
print(potencia)

nota = float(input("digite uma nota: "))
nota2 = float(input("digite outra nota: "))
nota3 = float(input("digite outra nota: "))
media = (nota + nota2 + nota3) / 3
print("a media do estudante é de: {:.2}".format(media))

produto = float(input("digite o valor do produto:R$ "))
parcelas = int(input("Escolha até quantas parcelas você vai querer de 1 a 10: "))
valor_final = produto / parcelas
print("O valor final do produto é de: {}".format(valor_final))