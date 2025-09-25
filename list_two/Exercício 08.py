# Escreva uma função que receba o raio de um círculo e retorne sua área. Utilize 3.14159 como valor para pi.

def calcular_area_circulo(raio):
    pi= 3.14159
    return pi * raio ** 2
raio= float(input('Digite o valor do raio: '))
area = calcular_area_circulo(raio)
print (f' A área com o raio de {raio} é de {area}.')

