d = int(input('Quantos dias você usou o carro? '))
km = float(input('Quantos KM o carro percorreu? '))
d = d * 60
km = km * 0.15
print(f'Você precisará pagar R${d:.2f} pelos dias que o carro foi alugado e R${km:.2f} pelos KM rodados.\nR${d + km:.2f} no total.')
