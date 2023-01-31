n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
if (n1 + n2) / 2 < 5.0:
    print('Reprovado.')
elif (n1 + n2) / 2 >= 5.0 and (n1 + n2) / 2 < 6.9:
    print('Recuperação.')
elif (n1 + n2) / 2 >= 7.0:
    print('Você foi aprovado!')
