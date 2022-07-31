v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print(f'Você foi multado. A multa é {(v - 80) * 7:.2f},00 reais.')
else:
    print('Você não foi multado.')
