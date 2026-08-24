# EXERCÍCIO 01
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = numero1 + numero2

print(f"O resultado da soma é: {resultado}")


# EXERCÍCIO 02
primeira_nota = float(input("Informe a primeira nota: ").replace(',', '.'))
segunda_nota = float(input("Informe a segunda nota: ").replace(',', '.'))

media_final = (primeira_nota + segunda_nota) / 2

print(f"Média calculada: {media_final:.1f}".replace('.', ','))


# EXERCÍCIO 03
numero = int(input("Informe um número inteiro: "))

anterior = numero - 1
proximo = numero + 1

print(f"Antecessor: {anterior}")
print(f"Valor informado: {numero}")
print(f"Sucessor: {proximo}")


# EXERCÍCIO 04
valor = float(input("Informe um número: ").replace(',', '.'))

dobro = valor * 2
triplo = valor * 3
metade = valor / 2

print(f"Dobro: {dobro:g}".replace('.', ','))
print(f"Triplo: {triplo:g}".replace('.', ','))
print(f"Metade: {metade:g}".replace('.', ','))


# EXERCÍCIO 05
medida_metros = float(input("Informe a medida em metros: ").replace(',', '.'))

medida_centimetros = medida_metros * 100
medida_milimetros = medida_metros * 1000

print(f"Em centímetros: {medida_centimetros:g}".replace('.', ','))
print(f"Em milímetros: {medida_milimetros:g}".replace('.', ','))


# EXERCÍCIO 06
base = float(input("Informe a largura do retângulo: ").replace(',', '.'))
altura = float(input("Informe a altura do retângulo: ").replace(',', '.'))

area_retangulo = base * altura
perimetro_retangulo = 2 * (base + altura)

print(f"Área do retângulo: {area_retangulo:g}".replace('.', ','))
print(f"Perímetro do retângulo: {perimetro_retangulo:g}".replace('.', ','))


# EXERCÍCIO 07
temperatura_celsius = float(
    input("Informe a temperatura em Celsius: ").replace(',', '.')
)

temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

print(
    f"Temperatura em Fahrenheit: {temperatura_fahrenheit:g}".replace('.', ',')
)


# EXERCÍCIO 08
valor_produto = float(
    input("Informe o preço do produto: R$ ")
    .replace('.', '')
    .replace(',', '.')
)

valor_desconto = valor_produto * 10 / 100
valor_com_desconto = valor_produto - valor_desconto

print(f"Valor do desconto: R$ {valor_desconto:.2f}".replace('.', ','))
print(f"Preço após desconto: R$ {valor_com_desconto:.2f}".replace('.', ','))


# EXERCÍCIO 09
salario_atual = float(
    input("Informe o salário atual: R$ ")
    .replace('.', '')
    .replace(',', '.')
)

valor_reajuste = salario_atual * 15 / 100
salario_reajustado = salario_atual + valor_reajuste

print(f"Valor do reajuste: R$ {valor_reajuste:.2f}".replace('.', ','))
print(f"Salário reajustado: R$ {salario_reajustado:.2f}".replace('.', ','))


# EXERCÍCIO 10
salario_base = float(
    input("Informe o salário fixo: R$ ")
    .replace('.', '')
    .replace(',', '.')
)

vendas_mes = float(
    input("Informe o valor total das vendas: R$ ")
    .replace('.', '')
    .replace(',', '.')
)

valor_comissao = vendas_mes * 4 / 100
pagamento_final = salario_base + valor_comissao

print(f"Comissão recebida: R$ {valor_comissao:.2f}".replace('.', ','))
print(f"Salário com comissão: R$ {pagamento_final:.2f}".replace('.', ','))


# EXERCÍCIO 14
valor_a = int(input("Informe o valor de A: "))
valor_b = int(input("Informe o valor de B: "))

temporario = valor_a
valor_a = valor_b
valor_b = temporario

print("Valores depois da troca:")
print(f"A = {valor_a}")
print(f"B = {valor_b}")


# EXERCÍCIO 15
valor_unitario = float(
    input("Informe o preço de cada produto: R$ ")
    .replace('.', '')
    .replace(',', '.')
)

qtd_produtos = int(input("Informe a quantidade comprada: "))

valor_frete = float(
    input("Informe o valor do frete: R$ ")
    .replace('.', '')
    .replace(',', '.')
)

valor_produtos = valor_unitario * qtd_produtos
valor_compra = valor_produtos + valor_frete

print(f"Subtotal dos produtos: R$ {valor_produtos:.2f}".replace('.', ','))
print(f"Valor final da compra: R$ {valor_compra:.2f}".replace('.', ','))