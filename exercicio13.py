# Exercício 13: Calcular gorjeta do restaurante
# Pedimos o valor da conta e convertemos para float.
valor_conta = float(input("Qual o valor total da conta do restaurante? R$ "))

# Calculamos 10% do valor da conta para a gorjeta.
valor_gorjeta = valor_conta * 0.10

# Calculamos o valor final somando a conta e a gorjeta.
valor_total = valor_conta + valor_gorjeta

# Exibimos os resultados formatados com duas casas decimais.
print(f"Valor da gorjeta (10%): R$ {valor_gorjeta:.2f}")
print(f"Valor total a pagar: R$ {valor_total:.2f}")

print("-" * 20)
