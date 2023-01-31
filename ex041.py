i = int(input('Qual sua idade? '))
if i <= 9:
    print('Você é da categoria mirim.')
elif i <= 14:
    print('Você é da categoria infantil.')
elif i <= 19:
    print('Você é da categoria junior.')
elif i == 20:
    print('Você é da categoria sênior.')
else:
    print('Você é da categoria master.')
