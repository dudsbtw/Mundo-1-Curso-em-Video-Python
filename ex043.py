p = float(input('Qual seu peso? '))
a = float(input('Qual sua altura? '))
imc = p / (a**2)
print(round(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Seu peso está um pouco acima do ideal.')
elif imc >= 30 and imc < 40:
    print('Você está obeso.')
elif imc >= 40:
    print('Você está com obesidade mórbida.')
