# Crie uma função que receba três números e retorne True se o primeiro for maior que o segundo e o segundo for maior que o terceiro, e False caso o contrário.

def verificacao_ordem(a,b,c):
    if a > b and b > c:
        return True
    else:
        return False
aa= int(input('Digite um número para a: '))
bb= int(input('Digite um número para b: '))
cc= int(input('Digite um número para c: '))
if verificacao_ordem(aa,bb,cc):
    print('True')
else:
    print('False')



