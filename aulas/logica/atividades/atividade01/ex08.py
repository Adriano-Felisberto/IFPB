"""Crie um algoritmo que efetue o cálculo do salário líquido de um professor. Os
dados fornecidos serão: valor da hora aula, número de aulas dadas no mês e
percentual de desconto do INSS."""

valor_hora = float(input("Digite o valor da hora aula: R$ "))
aulas_mes = int(input("Digite o número de aulas no mês: "))
des_inss = float(input("Digite o percentual de desconto do INSS: "))

salario_bruto = valor_hora * aulas_mes

desconto = (salario_bruto * des_inss) / 100

salario_liquido = salario_bruto - desconto

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do INSS: R$ {desconto:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
