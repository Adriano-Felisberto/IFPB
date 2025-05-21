"""Antes do racionamento de energia ser decretado, quase ninguém falava em quilowatts, 
mas agora, todos incorporaram essa palavra em seu vocabulário. 
Sabendo-se que 100 quilowatts de energia custa um sétimo do salário
 mínimo, faça um algoritmo que receba o valor do salário minimo
   e a quantidade de quilowatts gasta por uma residência,
   e calcule (imprima)

o valor em reais de cada quilowatt

o valor em reais a ser pago

o novo valor a ser pago por essa residência com um desconto de 10%"""

salaM = float(input("Digite o valor do salário mínimo: R$ "))
quant_quilow = float(input("Digite a quantidade de quilowatts consumidos: "))

valorq = (salaM / 7) / 100
totalvalor = valorq * quant_quilow
valordesc = (totalvalor * 10  ) / 100

print(f"Valor por quilowatt: R$ {valorq:.2f}")
print(f"Valor a ser pago: R$ {totalvalor:.2f}")
print(f"Valor com 10% de desconto: R$ {valordesc:.2f}")
