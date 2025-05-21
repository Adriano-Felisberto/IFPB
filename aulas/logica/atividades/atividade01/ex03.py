""" Escreva um programa que peça ao usuário um número natural que representa  
 o lado de um quadrado e calcule seu perímetro e a sua área."""
lado = float(input("Digite o valor em cm de um dos lados do quadrado: "))

perimetro = 4 * lado
area = lado ** 2

print(f"O perímetro do quadrado é {perimetro} cm.")
print(f"A área do quadrado é {area} cm².")
