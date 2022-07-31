nome = str(input('Digite seu nome completo: '))
nma = nome.upper()
nmi = nome.lower()
todo = len(nome) - nome.count(' ')
pn = nome.split()[0]
lpn = nome.find(' ')
print(f'Seu nome com todas as letras maiúsculas fica: {nma}.\n Seu nome com todas as letras minúsculas fica: {nmi}.\nSeu nome tem {todo} caracteres.\nSeu primeiro nome é: {pn} e ele tem {lpn} letras.')
