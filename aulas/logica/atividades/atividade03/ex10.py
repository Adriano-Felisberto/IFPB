"""Faça um programa que lê nome, estado civil e idade de uma pessoa. Se a
pessoa for casada e tiver menos de 25 anos, imprimir nome e a mensagem:
ACEITA. Caso contrário, imprimir o nome e a mensagem: NÃO ACEITA. (Para
o estado civil casado, o usuário deverá informar C ou c; para o estado civil
solteiro, o usuário deverá informar S ou s; para o estado civil divorciado, o
usuário deverá informar D ou d.)"""

nome = input("Digite o nome da pessoa: ")
estado_civil = input("Digite o estado civil (C/c para casado, S/s para solteiro, D/d para divorciado): ")
idade = int(input("Digite a idade da pessoa: "))

if (estado_civil == "C" or estado_civil == "c") and idade < 25:
    print(f"{nome} - ACEITA")
else:
    print(f"{nome} - NÃO ACEITA")
