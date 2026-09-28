# LISTA DE EXERCÍCIOS: FUNÇÕES & MÓDULOS EM PYTHON
# Algoritmos e Programação em Python
# ============================================================

import math
import time

# Função utilitária para aguardar 10 segundos antes de fechar
def aguardar_fechamento():
    print("\nEste programa será fechado em 10 segundos...")
    time.sleep(10)

# EXERCÍCIO 1: Arredondamento e Raiz Quadrada
def exercicio_1():
    print("\n===== EXERCÍCIO 1: Arredondamento e Raiz Quadrada =====")
    numero = float(input("Digite um número decimal positivo: "))

    raiz = math.sqrt(numero)
    arredondado_cima = math.ceil(numero)
    arredondado_baixo = math.floor(numero)

    print(f"Raiz quadrada de {numero}: {raiz:.4f}")
    print(f"Valor arredondado para cima: {arredondado_cima}")
    print(f"Valor arredondado para baixo: {arredondado_baixo}")

    aguardar_fechamento()

# EXERCÍCIO 2: Calculadora de Área de Círculo
def calcular_area_circulo(raio):
    return math.pi * (raio ** 2)

def exercicio_2():
    print("\n===== EXERCÍCIO 2: Calculadora de Área de Círculo =====")
    raio = float(input("Digite o valor do raio do círculo: "))
    area = calcular_area_circulo(raio)
    print(f"A área do círculo de raio {raio} é: {area:.2f}")

    aguardar_fechamento()

# EXERCÍCIO 3: Parâmetros e Condicionais (Maior de Três)
def encontrar_maior(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def exercicio_3():
    print("\n===== EXERCÍCIO 3: Maior de Três Números =====")
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))
    c = int(input("Digite o terceiro número inteiro: "))

    maior = encontrar_maior(a, b, c)
    print(f"O maior valor entre {a}, {b} e {c} é: {maior}")

    aguardar_fechamento()


# EXERCÍCIO 4: Compreendendo Escopo de Variáveis
def exercicio_4():
    print("\n===== EXERCÍCIO 4: Escopo de Variáveis =====")

    x = 10  # Variável 1 (escopo global)

    def alterar_valor():
        x = 5  # Variável 2 (escopo local, sombreia a global)
        print(f"Valor dentro da função: {x}")

    alterar_valor()
    print(f"Valor fora da função: {x}")

    print("\n--- RESPOSTA A ---")
    print("Valor dentro da função: 5")
    print("Valor fora da função: 10")

    print("\n--- RESPOSTA B ---")
    print("O valor de x fora da função não é alterado para 5 porque, em Python,")
    print("variáveis atribuídas dentro de uma função possuem escopo LOCAL.")
    print("A linha 'x = 5' cria uma NOVA variável local chamada x, que só existe")
    print("dentro da função alterar_valor(). A variável global x = 10 permanece")
    print("intacta no escopo global. Para alterar a global, seria necessário usar")
    print("a palavra-chave 'global x' dentro da função.")

    aguardar_fechamento()

# EXERCÍCIO 5: Desafio Integrador (Cálculo de Hipotenusa)
def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt((cateto_a ** 2) + (cateto_b ** 2))

def exercicio_5():
    print("\n===== EXERCÍCIO 5: Cálculo de Hipotenusa =====")
    cateto_a = float(input("Digite o valor do primeiro cateto: "))
    cateto_b = float(input("Digite o valor do segundo cateto: "))

    hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
    print(f"A hipotenusa do triângulo retângulo é: {hipotenusa:.2f}")

    aguardar_fechamento()

# MENU PRINCIPAL (para executar todas as atividades)
def main():
    while True:
        print("\n" + "=" * 50)
        print("LISTA DE EXERCÍCIOS: FUNÇÕES & MÓDULOS")
        print("=" * 50)
        print("1 - Exercício 1: Arredondamento e Raiz Quadrada")
        print("2 - Exercício 2: Calculadora de Área de Círculo")
        print("3 - Exercício 3: Maior de Três")
        print("4 - Exercício 4: Escopo de Variáveis")
        print("5 - Exercício 5: Cálculo de Hipotenusa")
        print("0 - Sair")
        print(  "=" * 50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exercicio_1()
        elif opcao == "2":
            exercicio_2()
        elif opcao == "3":
            exercicio_3()
        elif opcao == "4":
            exercicio_4()
        elif opcao == "5":
            exercicio_5()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()