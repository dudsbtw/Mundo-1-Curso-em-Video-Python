r = False
while r == False:
    a = input('Digite algo: ')
    print(f'O tipo primitivo é: {type(a)}')
    print(f'Só tem espaços? {a.isspace()}')
    print(f'É alfabético? {a.isalpha()}')
    print(f'É alfanúmerico? {a.isalnum()}')
    print(f'Está em maiúsculas? {a.isupper()}')
    print(f'Está em minúsculas? {a.islower()}')
    print(f'Está capitalizada? {a.istitle()}')
