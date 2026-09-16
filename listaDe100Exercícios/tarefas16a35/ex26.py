print("=== Exercício 26: Reajuste por Faixa Salarial ===")
salario = float(input("Salário atual: R$ "))
if salario <= 1500:
    p = 15
elif salario <= 3000:
    p = 10
else:
    p = 5
aumento = salario * p / 100
novo = salario + aumento
print(f"Percentual aplicado: {p}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo:.2f}")