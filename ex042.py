r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima formam um triângulo ', end='')
    if r1 == r2 and r2 == r3:
        print('equilátero.')
    if r1 != r2 and r2 != r3 and r1 != r3:
        print('escaleno.')
    if r1 == r2 or r1 == r3 or r2 == r3:
        print('isósceles.')
else:
    print('Os segmentos acima não formam um triângulo.')
