"""Faça um programa que faça o mesmo que o programa anterior, mas agora
solicitando Strings ao usuário."""

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

print(f"\nResultados de '{str1}' em relação a '{str2}':")
print(f"'{str1}' == '{str2}' → {str1 == str2}")
print(f"'{str1}' != '{str2}' → {str1 != str2}")
print(f"'{str1}' > '{str2}'  → {str1 > str2}")
print(f"'{str1}' < '{str2}'  → {str1 < str2}")
print(f"'{str1}' >= '{str2}' → {str1 >= str2}")
print(f"'{str1}' <= '{str2}' → {str1 <= str2}")

print(f"Resultados de '{str2}' em relação a '{str1}':")
print(f"'{str2}' == '{str1}' → {str2 == str1}")
print(f"'{str2}' != '{str1}' → {str2 != str1}")
print(f"'{str2}' > '{str1}'  → {str2 > str1}")
print(f"'{str2}' < '{str1}'  → {str2 < str1}")
print(f"'{str2}' >= '{str1}' → {str2 >= str1}")
print(f"'{str2}' <= '{str1}' → {str2 <= str1}")
