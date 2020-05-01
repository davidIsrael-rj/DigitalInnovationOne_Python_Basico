a = int(input('Primeiro bimestre: '))
if a>10:
    a=int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b>10:
    b=int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c>10:
    c=int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d>10:
    d=int(input('Você digitou errado. Quarto bimestre: '))
media = (a+b+c+d)/4
if a<=10 and b<=10 and c<=10 and d<=10:
    print('Media: {}'.format(media))
else:
    print('Foi informado alguma nota errada')

# a=int(input('Entre com um numero: '))
# b=int(input('Entre com o segundo valor: '))
#
# resto_a = a%2
# resto_b = b%2
# if resto_a == 0 or resto_b ==0:
#     #print('O numero : {} é par'.format(a))
#     print('foi digitado um numero par')
# else:
#     print('Nenhum numero par foi digitado')
    #print('O numero: {} é impar'.format(a))
# a = int(input('Valor de A: '))
# b = int(input('Valor de B: '))
# c = int(input('Valor de C: '))
#
# if a>b and a>c:
#     print('O maior numero é A : {}'.format(a))
# elif b>a and b>c:
#     print('O maior numero é B : {}'.format(b))
# else:
#     print('O maior numero é C : {}'.format(c))
# print('Final do programa')