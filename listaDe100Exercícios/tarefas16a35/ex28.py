print("=== Exercício 28: É Possível Formar um Triângulo? ===")
a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))
if a < b + c and b < a + c and c < a + b:
    print("Resultado: FORMAM UM TRIÂNGULO")
else:
    print("Resultado: NÃO FORMAM")