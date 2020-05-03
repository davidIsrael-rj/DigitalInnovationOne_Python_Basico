class Televisao:
#no python não existe diferença entre metodos e função
# função é tudo que retorna valor e metodo não
# no python as funções são definição = def
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
           self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

televisao = Televisao()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão estáligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {} '.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.power()
print('Televisão está ligada: {} '.format(televisao.ligada))
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal))
televisao.diminui_canal()
print('Canal: {}'.format(televisao.canal))