palavra = input("Digite uma palavra: ")

# Lista de todas as consoantes em português
listaconso = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

# Exemplo: contar quantas consoantes a palavra tem
cont = 0
for letra in palavra.lower():
    if letra in listaconso:
        cont += 1

print(f"A palavra '{palavra}' tem {cont} consoante(s).")
