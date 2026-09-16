print("=== Exercício 29: Tipo de Triângulo ===")
a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("EQUILÁTERO")
    elif a == b or a == c or b == c:
        print("ISÓSCELES")
    else:
        print("ESCALENO")
else:
    print("NÃO FORMA TRIÂNGULO")