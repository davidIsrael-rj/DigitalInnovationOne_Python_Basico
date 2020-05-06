#importando um modulo
#importamos o modulo e sua classe
from Aula7_televisao import Televisao
from Aula7_calculadora1 import Calculadora
#importamos um modulos e seus metodos
from Aula8_contador_letras import contador_letras, teste
print('De onde está sendo executado {}'.format(__name__))
if __name__ == '__main__':
    print('De onde está sendo executado {}'.format(__name__))
    televisao = Televisao()
    print('A televisa esta ligada {}'.format(televisao.ligada))
    televisao.power()
    print('A televisao esta ligada {}'.format(televisao.ligada))

    calculadora = Calculadora(5, 10)
    print('A soma de {} + {} = {}'.format(calculadora.valor_a, calculadora.valor_b,calculadora.soma()))

    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista))

    print(teste())


