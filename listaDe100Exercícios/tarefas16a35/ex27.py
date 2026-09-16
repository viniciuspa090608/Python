print("=== Exercício 27: Classificação de IMC ===")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)
print(f"IMC: {imc:.1f}")
if imc < 18.5:
    print("Classificação: ABAIXO DA FAIXA")
elif imc < 25:
    print("Classificação: FAIXA NORMAL")
elif imc < 30:
    print("Classificação: ACIMA DA FAIXA")
else:
    print("Classificação: FAIXA ELEVADA")