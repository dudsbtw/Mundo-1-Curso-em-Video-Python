from time import localtime
a = int(input('Digite o seu ano de nascimento: '))
idade = localtime().tm_year - a
atual = localtime().tm_year #2023
if idade < 18:
    saldo = 18 - idade
    print('Você ainda vai se alistar!')
    print(f'Ainda faltam {18 - idade} anos para o alistamento obrigatório.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print('Você já passou da idade de alistamento!')
    print(f'Você está {saldo} anos atrasado.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
else:
    print('É hora de se alistar!')
