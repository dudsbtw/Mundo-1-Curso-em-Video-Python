vc = float(input('Insira o valor da casa: '))
s = float(input('Insira o seu salário: '))
a = int(input('Em quantos anos você vai pagar: '))
p = vc / (a * 12)
if vc / (a * 12) > s * 0.30:
    print('Emprestimo não concedido.')
    print(f'Você teria que pagar R${p:.2f} por mês, isso excede 30% do seu salário.')
else:
    print('Emprestimo concedido.')
    print(f'Você pagará R${p:.2f} por mês.')
