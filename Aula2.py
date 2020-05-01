#a = 10
#b = 5
#entrando com valor do usuario e convertendo para inteiro
a= int(input('Entre com o primeiro valor:'))
b=input('entre com o segundo valor:')
#a=int(a)
b=int(b)
soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b
resto = a%b
#serve para comentar
print('soma: {} subtracao: {}'.format(soma,subtracao))
print('soma: {soma} \nsubtracao: {subtracao}'.format(soma=soma,subtracao=subtracao))
print(type(soma))
soma = str(soma)
print(type(soma))
print('soma: '+ str(soma))
print(soma)
print(subtracao)
print(multiplicacao)
print(type(divisao))
print(int(divisao))
print(divisao)
print(resto)
x = '1'
soma2 = int(x) +1
print(soma2)