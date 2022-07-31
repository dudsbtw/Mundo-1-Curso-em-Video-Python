d = int(float(input('Digite a distância da viagem em KM: ')))
if d <= 200:
    d = d * 0.50
else:
    d = d* 0.45
print(f'O valor da passagem é R${d:.2f}.')
