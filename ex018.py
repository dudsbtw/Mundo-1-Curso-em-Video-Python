from math import sin, cos, tan, radians
an = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(an))
print(f'O ângulo de {an} tem o seno de {s:.2f}.')
c = cos(radians(an))
print(f'O ângulo de {an} tem o cosseno de {c:.2f}.')
t = tan(radians(an))
print(f'O ângulo de {an} tem a tangente de {t:.2f}.')
