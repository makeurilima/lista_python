# Escreva uma função que receba o valor de um produto e retorne o valor final com um acréscimo de 15 % de imposto.

def acrescimo_imposto(valor):
    imposto = 0.15
    return valor * imposto
valor_produto = float(input("Digite o valor do produto: "))
acrescimo = valor_produto * 0.15
valor_total = valor_produto + acrescimo
print(f'O acréscimo do imposto será de: R$ {acrescimo_imposto(valor_produto)}')
print(f'Portanto o valor final com o imposto será de {valor_total}')


