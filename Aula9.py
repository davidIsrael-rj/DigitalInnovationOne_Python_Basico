import shutil
#criar um arquivo, ou sobrescrever um existente
def escrever_arquivo(texto):
    #dessaforma vc escolhe aonde ira gerar um arquivo
    diretorio = '/home/dyas/InnovationOne/Python/Python_Basico/teste.txt'
    arquivo = open(diretorio, 'w')
    #dessa forma vc gera o arquivo no mesmo diretorio aonde esta executando o codigo
    #arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

#criar um arquivo ou atualizar um existente
def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

#fazendo a leitura de um arquivo
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    # transformando em uma lista através do split
    # a cada enter '\n' sela um elemento diferente
    aluno_nota = aluno_nota.split('\n')
    print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        #separando os elementos pela virgula ','
        lista_notas = x.split(',')
        #print(lista_notas)
        aluno = lista_notas[0]
        #retirando o nome
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas])/4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
    arquivo.close()

#copiando um arquivo para uma pasta especifica
def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '/home/dyas/InnovationOne/Python/App_Python2/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,'/home/dyas/InnovationOne/Python/App_Python2/')

if __name__ == '__main__':
    move_arquivo('alunos.txt')
    #copia_arquivo('alunos.txt')
    #lista_media = media_notas('alunos.txt')
    #print(lista_media)

    #escrever_arquivo('Primeira linha\n')
    #atualizar_arquivo('Terceira linha\n')
    #aluno ='Cesar,7,9,3,8\n'
    #atualizar_arquivo('alunos.txt',aluno)
    #ler_arquivo('teste.txt')