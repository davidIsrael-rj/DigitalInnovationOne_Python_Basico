class Calculadora:
    #não a necessidade de ter pois ñ ira inicializar nada
    # def __init__(self):
    #     pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(100, 47))
print(calculadora.multiplicacao(30, 25))
print(calculadora.divisao(1000, 5))