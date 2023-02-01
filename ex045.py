import random
from time import sleep
esc = ['Pedra', 'Papel', 'Tesoura']
com = random.choice(esc)
eu = input('Pedra, papel ou tesoura? ').lower()
print('Jo')
sleep(0.7)
print('Ken')
sleep(0.7)
print('Po!')
sleep(0.25)
if com == 'Pedra':
    if eu == 'pedra':
        print('Empate.')
    if eu == 'papel':
        print('Venceu!')
    if eu == 'tesoura':
        print('Perdeu.')
if com == 'Papel':
    if eu == 'pedra':
        print('Perdeu.')
    if eu == 'papel':
        print('Empate.')
    if eu == 'tesoura':
        print('Ganhou!')
if com == 'Tesoura':
    if eu == 'pedra':
        print('Venceu!')
    if eu == 'papel':
        print('Perdeu.')
    if eu == 'tesoura':
        print('Empate.')
if eu != 'papel' and eu != 'tesoura' and eu != 'pedra':
    print('Escolha inválida.')
sleep(2)
print(f'Você escolheu {eu} e o computador escolheu {com}!')
