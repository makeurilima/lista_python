# Escreva uma função que receba um valor em metros e o retorne convertido para centímetros.

def conversao_metros_centimetros(valor, cent= 100):
    return valor * cent

valor_em_metros = float(input('Digite o valor em metros: '))
valor_em_centimetros = valor_em_metros * 100

print (f'O valor de {valor_em_metros}m convertido em centímetros é {valor_em_centimetros} cm.')

