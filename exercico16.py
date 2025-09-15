# Exercício 16: Calcular média de três notas
# Pedimos as três notas e as convertemos para float.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculamos a média aritmética simples.
media = (nota1 + nota2 + nota3) / 3

# Exibimos o resultado da média com duas casas decimais.
print(f"A média das notas {nota1}, {nota2} e {nota3} é {media:.2f}.")

print("-" * 20)


