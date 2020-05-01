conjunto = {1,2,3,4,5}
conjunto2={5,6,7,8}
conjunto_uniao= conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é um subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante', 'elefante']
#converter lista em conjuntos
conjunto_animais = set(lista)
#converter conjunto em lista
lista_animais= list(conjunto_animais)
#converter lista em tuplas
tuplas_animais= tuple(lista_animais)
print(conjunto_animais)
print(lista_animais)
print(tuplas_animais)
# conjunto = {1,2,3,4}
# print(type(conjunto))
# #adicionado elemento
# conjunto.add(5)
# #removendo elemento
# conjunto.discard(2)
# print(conjunto)