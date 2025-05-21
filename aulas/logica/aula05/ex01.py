Num = int(input("Digite um número: "))
calculo = Num % 2
calculo3 = Num % 3

if calculo == 0:
    print("É divisível por dois")
elif calculo3 == 0:
    print("É divisível por Três")
elif Num % 2 == 0 or Num % 3 == 0:
    print("o numero é divisivel por um dos dois numeros(2 ou 3)")
else:
    print("Esse número não é divisível por Dois e por Três")
