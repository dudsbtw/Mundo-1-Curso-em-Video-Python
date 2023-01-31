n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
if n1 > n2:
    print(f'O primeiro valor ({n1})) é maior.')
elif n1 < n2:
    print(f'O segundo valor ({n2}) é maior.')
else:
    print(f'Os valores ({n1} e {n2}) são iguais.')
