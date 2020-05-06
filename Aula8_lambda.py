#lambida é uma função anonima e é um modo de
# simplificar o que utilizaremos
# varias vezes no código
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

somaA = lambda a, b: a + b
subtracao = lambda a, b: a - b

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao':lambda a, b: a * b,
    'divisao':lambda a, b: a / b,
}

print(type(calculadora))
somaB = calculadora['soma']
#somaB = lambda a, b: a + b
multiplicacao = calculadora['multiplicacao']
print('A multiplicação é: {}'.format( multiplicacao(10, 3)))
print('A soma é : {}'.format(somaA(10, 5)))
print('A soma é : {}'.format(somaB(5, 10)))
print('A subtração é : {}'.format(subtracao(8,2)))