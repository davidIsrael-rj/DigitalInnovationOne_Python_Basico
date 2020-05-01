lista = [12,3,52,7]
lista_animal = ['cachorro', 'gato', 'elefante','lobo', 'arara']
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
lista_animal.reverse()
print(lista_animal)
tupla = (1,10,12,14)
print(tupla[0])
print(len(tupla))
print(len(lista_animal))
tupla_animal=tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica=list(tupla)
print(type(lista_numerica))
print(lista_numerica)
lista_numerica[0]=100
print(lista_numerica)

# print(lista_animal[1])
#
# for x in lista_animal:
#     print('animal {}'.format(x))
#
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
# print('utilizando auto soma')
# print(sum(lista))
# print('imprimir valor maximo')
# print(max(lista))
# print('menor valor')
# print(min(lista))
#verificando se existe um gato na lista
# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista ')
#     lista_animal.append('lobo')
#     print(lista_animal)
# lista_animal.pop(2)
# print(lista_animal)
#nova_lista = lista_animal * 3
#print(nova_lista)
#remover pelo nome
#lista_animal.remove('gato')
#print(lista_animal)