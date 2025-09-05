num = [1, 2, 3, 4, 5]

for i in range(len(num)):
    num[i] = num[i] + 2
    print(num[i])

a = [1,2, 3]
b = [4, 5, 6]
c = a + b # une ambas as listas em uma só se somar a lista com outra
print(c)

print(a * 2) # com multiplicação, a lista é repetida
#só é possivel somar e multiplicar quando é uma interação de listas

letras = ['p', 'y', 't', 'h', 'o', 'n']
letras.pop() # remove o ultimo elemento da lista
print(letras)
letras.pop(2) # remove o elemento do indice 2
print(letras)
letras.remove('y') # remove o elemento 'y' da lista
print(letras)
print(letras[1:3]) # fatiamento, pega do indice 1 ao 3
print(letras[-1]) # pega o ultimo elemento da lista
print(letras[-3:]) # pega os 3 ultimos elementos da lista
print(letras[:4]) # pega todos os elementos menos os 4 ultimos
print(letras[::2]) # pula de 2 em 2
print(letras[::-1]) # inverte a lista

del letras[0] # deleta o primeiro elemento da lista
print(letras)
del letras[1:3] # deleta do indice 1 ao 3
print(letras)