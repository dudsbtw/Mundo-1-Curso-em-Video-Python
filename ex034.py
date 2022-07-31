s = float(input('Digite seu salário: '))
if s <= 1250:
    print('Você recebeu um aumento de 15%.')
    s = s + (s * 15 / 100)
    print(f'Seu novo salário é de R$ {s:.2f}.')
else:
    print('Você recebeu um aumento de 10%.')
    s = s + (s * 10 / 100)
    print(f'Seu novo salário é de R$ {s:.2f}.')
