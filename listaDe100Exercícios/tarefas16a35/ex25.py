print("=== Exercício 25: Preço Conforme Forma de Pagamento ===")
preco = float(input("Preço: R$ "))
opcao = int(input("Opção (1-Dinheiro/Pix, 2-Débito, 3-Crédito à vista, 4-Crédito parcelado): "))
if opcao == 1:
    final = preco * 0.90
elif opcao == 2:
    final = preco * 0.95
elif opcao == 3:
    final = preco
else:
    final = preco * 1.08
print(f"Valor final: R$ {final:.2f}")