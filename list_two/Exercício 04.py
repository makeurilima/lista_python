# Crie uma função que calcule a área de um retângulo, recebendo a base e a altura como parâmetros.

def area_retangulo (base, altura):
    return base * altura

largura = int(input('Digite a base do retângulo em cm: '))
comprimento = int(input('Digite a altura do retângulo em cm: '))
area = largura * comprimento

print (f'A área deste retângulo é {area} cm.')
