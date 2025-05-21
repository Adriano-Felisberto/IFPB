"""Escreva um programa que peça ao usuário dois números naturais
 para as  variáveis A e B, e efetue as trocas dos valores de forma que a variável
 A passe  a possuir o valor da variável B e a variável B passe a possuir o valor da variável  A.
 Apresentar os valores trocados. OBS: não é permitido apenas imprimir o valor  trocado. 
 Ex.: “O valor da variável A é: “ e imprimir da variável B. 
"""
A = int(input(""))
B = int(input(""))
temp = A
A = B

print(A)
B = A
print(temp)