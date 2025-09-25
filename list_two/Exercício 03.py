# Crie uma função que receba um número e retorne seu valor ao quadrado.

def potencia (base, expoente = 2):
    return base ** expoente

algoritmo = int(input('Digite um algoritmo: '))
potenciacao = algoritmo ** 2

print(f'O resultado de {algoritmo} elevado ao quadrado é {potenciacao}.')
