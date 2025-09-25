# Crie uma função que converta um valor em horas para minutos.

def conversao_horas_minutos(horas, minutos = 60):
    return horas * minutos
hora = int(input('Digite a quantidade de horas: '))
print(conversao_horas_minutos(hora, 60))
