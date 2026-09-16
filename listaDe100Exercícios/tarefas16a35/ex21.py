print("=== Exercício 21: Aprovado ou Reprovado ===")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2
print("Média:", media)
if media >= 7:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")