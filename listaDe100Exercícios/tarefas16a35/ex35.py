print("=== Exercício 35: Valor do Ingresso ===")
idade = int(input("Idade: "))
estudante = input("Estudante (SIM/NÃO): ").upper()
if idade < 12 or estudante == "SIM" or idade >= 60:
    print("Valor do ingresso: R$ 15,00")
else:
    print("Valor do ingresso: R$ 30,00")