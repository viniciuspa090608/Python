print("=== Exercício 30: Aprovação de Empréstimo ===")
valor = float(input("Valor do imóvel: R$ "))
salario = float(input("Salário: R$ "))
anos = int(input("Prazo (anos): "))
prestacao = valor / (anos * 12)
limite = salario * 0.30
print(f"Prestação: R$ {prestacao:.2f}")
print(f"Limite (30% do salário): R$ {limite:.2f}")
if prestacao <= limite:
    print("Resultado: APROVADO")
else:
    print("Resultado: NEGADO")