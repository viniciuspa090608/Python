print("=== Exercício 22: Situação do Aluno por Faixa ===")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2
print("Média:", media)
if media < 5:
    print("Situação: REPROVADO")
elif media < 7:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: APROVADO")