print("=== Exercício 23: Categoria de Votação ===")
idade = int(input("Idade: "))
if idade < 16:
    print("NÃO PODE VOTAR")
elif idade < 18:
    print("VOTO OPCIONAL")
elif idade < 70:
    print("VOTO OBRIGATÓRIO")
else:
    print("VOTO OPCIONAL")