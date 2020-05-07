# tratando erros
lista = [1,10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    #vai da erro por divisão por zero
    divisao = 10 / 0
    #vai dar erro ao acessar um elemento que não existe
    #numero = lista[3]
    #Recebendo uma variavel que não existe
    #x = a
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
#except NameError:
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
    #print('Tentando ler uma variavel que não existe')
except:
    print('Erro desconhecido')
else:
    print('Executa quando não ocorrer exceção')
finally:
    print('Sempre executa, independente se tiver erro ou não')
    print('Fechando arquivo')
    arquivo.close()