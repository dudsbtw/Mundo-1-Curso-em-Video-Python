m = float(input('Digite o tamanho em metros: '))
dm = m * 10
c = m * 100
mm = m * 1000
km = m / 1000
hm = m / 100
dam = m / 10
print(f'{m} metros em decímetros é: {dm:.1f}.')
print(f'{m} metros em milímetros é: {mm:.1f}.')
print(f'{m} metros em centímetros é: {c:.1f}.')
print(f'{m} metros em decâmetros é: {dam:.1f}.')
print(f'{m} metros em hectômetros é: {hm:.1f}.')
print(f'{m} metros em kilômetros é: {km:.2f}.')
