# Exercício 9: Somar dois números inteiros
# Pedimos ao usuário para digitar dois números.
# A função input() sempre retorna texto (string), então usamos int() para converter para inteiro.
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Realizamos a soma.
soma = numero1 + numero2

# Exibimos o resultado.
print(f"A soma de {numero1} + {numero2} é igual a {soma}.")

print("-" * 20)
