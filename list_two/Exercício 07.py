# Crie uma função que receba uma string e um número inteiro, e retorne a string repetida o número de vezes informado.

def repetir_strings(texto, vezes):
    return texto * vezes
mensagem = str(input('Digite algo: '))
vezes_repetidas = int(input('Digite a quantidade de vezes: '))
print(repetir_strings(mensagem, vezes_repetidas))

