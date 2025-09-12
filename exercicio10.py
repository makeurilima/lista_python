# Exercício 10: Calcular idade aproximada
# Definimos o ano atual em uma variável.
ano_corrente = 2025
# Pedimos o ano de nascimento e o convertemos para inteiro.
ano_nascimento = int(input("Em que ano você nasceu? "))

# Calculamos a idade subtraindo o ano de nascimento do ano atual.
idade_aproximada = ano_corrente - ano_nascimento

# Exibimos o resultado.
print(f"Você tem ou fará aproximadamente {idade_aproximada} anos em {ano_corrente}.")

print("-" * 20)
