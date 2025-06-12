"""Crie um algoritmo em Python que solicite o nome e 3 notas de cada aluno de
uma turma de 20 alunos, e imprima:
○ média de cada aluno;
○ a média da turma;
○ o percentual de alunos aprovados (alunos que tiveram médias superiores
ou iguais a 5.0)."""
alunos = []
soma_medias = 0
aprovados = 0

for i in range(0, 20, +1):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    notas = []
    for n in range(0, 3, +1):
        nota = float(input(f"Digite a nota {n+1} do aluno {nome}: "))
        notas.append(nota)
    
    media = sum(notas) / 3
    soma_medias += media

    if media >= 5.0:
        aprovados += 1

    alunos.append((nome, media))

print("\nMédia de cada aluno:")
for nome, media in alunos:
    print(f"{nome}: {media:.2f}")

media_turma = soma_medias / 20
percentual_aprovados = (aprovados / 20) * 100

print(f"\nMédia da turma: {media_turma:.2f}")
print(f"Percentual de alunos aprovados: {percentual_aprovados:.1f}%")

