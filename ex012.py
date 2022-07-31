p = float(input('Digite o valor de um produto: R$'))
d = 5
r = d * p / 100
print(f'O produto custa: R${p:.2f}.\nO valor do desconto é: R${r:.2f}.\nO valor do produto com 5% de desconto é: R${p - r:.2f}.')
