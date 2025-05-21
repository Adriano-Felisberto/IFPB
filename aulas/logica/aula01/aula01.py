inte = int(15)
string_conv = str(inte)
print(string_conv)

idade = int(input("Digite uma idade: "))
print("Sua idade é de: {}".format(idade))
print(idade + 99)

while True:
    nome = input("Digite o nome de usuário: ").upper()
    print("O nome digitado é: {}".format(nome))
    if nome == "ADRIANO":
        print("Acesso permitido")
        break
    else:
        print("Acesso negado")
