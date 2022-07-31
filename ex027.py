nome = str(input('Qual seu nome? ')).strip()
n = nome.split() 
print(f'Seu primeiro nome é {n[0]}.\nSeu último nome é {n[-1]}.')
