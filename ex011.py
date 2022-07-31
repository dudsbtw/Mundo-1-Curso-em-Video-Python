from re import A


a = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))
ar = a * l
tn = ar / 2
print(f'A dimensão da parede é {a}m x {l}m.')
print(f'A área da parede é: {ar}m².')
print(f'A quantidade de latas de tinta necessárias é: {tn}m².')
