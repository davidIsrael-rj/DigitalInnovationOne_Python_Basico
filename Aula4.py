a = int(input('Primeiro bimestre: '))
while a>10:
    a=int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b>10:
    b=int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c>10:
    c=int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d>10:
    d=int(input('Você digitou errado. Quarto bimestre: '))
media = (a+b+c+d)/4
if a<=10 and b<=10 and c<=10 and d<=10:
    print('Media: {}'.format(media))
else:
    print('Foi informado alguma nota errada')
# nota = int(input('Entre com a nota: '))
# while nota >10:
#     nota = int(input('Nota inválida. Entre com a nota correta: '))
# print(nota)
# a=0
# while a < 10:
#     print(a)
#     a += 1
# b=int(input('Entre com um numero: '))
# for a in range(b):
#     div = 0
#     cont = 0
#     for x in range(1, a + 1):
#         resto = a % x
#         divisao = a / x
#         divisao_1 = int(divisao)
#     #    if resto == 0:
#      #       print('{} / {} = {} resto {}'.format(a, x, divisao_1, resto))
#         if resto == 0:
#             # div = div + 1
#             div += 1
#     if div == 2:
#         cont += 1
#         print('Número {} é primo'.format(a))
#
# print(cont)
    #else:
     #   print('Número {} não é primo'.format(a))

# a = int(input('Entre com o numero: '))
#
# div =0
# for x in range(1, a+1):
#     resto = a % x
#     divisao = a / x
#     divisao_1=int(divisao)
#     if resto==0:
#         print('{} / {} = {} resto {}'.format(a,x,divisao_1,resto))
#     if resto ==0:
#         #div = div + 1
#         div += 1
# if div ==2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))
#
# print('aula 4')
# for x in range(1, 101):
#     print(x)