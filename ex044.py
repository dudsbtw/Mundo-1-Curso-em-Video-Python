p = float(input('Qual o preço do produto? '))
print('Selecione como pagará pelo produto:\n1 - Dinheiro / Cheque.\n2 - À vista no cartão.\n3 - Em até 2 parcelas no cartão.\n4 - 3 ou mais parcelas no cartão.')
pp = float(input())
if pp == '1':
    ppp = (10 / 100) * p
    print('Você recebeu 10''%'f' de desconto! O produto que antes custava R${p:.2f} agora custa R${p - ppp:.2f}.')
elif pp == 2:
    ppp = (5 / 100) * p
    print('Você recebeu 5''%'f' de desconto! O produto que antes custava R${p:.2f} agora custa R${p - ppp:.2f}.')
elif pp == 3:
    print(f'Você pagará R${p:.2f}, o preço normal.')
elif pp == 4:
    ppp = (20 / 100) * p
    print('Você terá que pagar 20''%'f' de juros. O produto que antes custava R${p:.2f} agora custa {p + ppp:.2f}.' )
