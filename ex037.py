n = int(input('Digite um número: '))
r = input('1: Binário\n2: Octal\n3: Hexadecimal\n')
if r == '1':
    print(f'O número {n} em binário é {bin(n)[2:]}.')
elif r == '2':
    print(f'O número {n} em octal é {oct(n)[2:]}.')
elif r == '3':
    print(f'O número {n} em hexadecimal é {hex(n)[2:]}.')
else:
    print('Opção inválida.')
