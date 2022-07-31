import random
na = random.randint(0,5)
n = False
while n == False:
    c = int(input('Digite um valor: '))
    if c > na:
        print('O valor inserido foi maior que o valor gerado.')
    elif c < na:
        print('O valor inserido foi menor que o valor gerado.')
    elif c == na:
        n = True
        print('Você acertou!')
