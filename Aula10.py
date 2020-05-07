#Trabalhando com Data
#Iremos importar alguns recursos sobre Datas

from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    #iremos pegar a data atual e logo apos exibi-la
    data_atual = date.today()
    print(data_atual)
    #formatando a data para o padrao brasileiro
    #pra utilizar a formatação visualizar a documentação
    #https://docs.python.org/pt-br/3/library/datetime.html#strftime-and-strptime-behavior
    print(data_atual.strftime('%d/%m/%Y'))
    data_atual_str = data_atual.strftime('%A %b %Y')
    #convertendo a data para string
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))
def trabalhando_com_time():
    #criando uma hora
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    #formatando a hora
    print(horario.strftime('%H:%M:%S'))
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario))
    print(horario_str)
    print(type(horario_str))


def trabalhando_com_datetime():
    #ira trazer a data e o horário atual
    data_atual = datetime.now()
    print(data_atual)
    #formatando para exibir somente a data
    print(data_atual.strftime('%d/%m/%Y'))
    #formatando para exibir somente o horário
    print(data_atual.strftime('%H:%M:%S'))
    #trazendo somente o dia
    print('Hoje é dia {}'.format(data_atual.day))
    #trazendo somente o ano
    print('Estamo no ano {}'.format(data_atual.year))
    #trazendo o numero do dia da semana
    print(data_atual.weekday())
    #imprimindo o dia da semana em português
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    #criar uma data com ano, mês, dia, hora, minutos, e segundos
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    #data formatada
    print(data_criada.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_criada.strftime('%c'))
    #convertendo data de string para datetime
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    #verificando se converteu para datetime
    print(type(data_convertida))

def trabalhando_com_timedelta():
    #diminuindo um ano da data atual
    nova_data = datetime.now() - timedelta(days=366)
    #convertendo para ao formato brasileiro
    nova_data = nova_data.strftime('%d/%m/%Y')
    #exibindo a data atual
    print(nova_data)

def somando_data(data):
    data_convertida = datetime.strptime(data, '%d/%m/%Y')
    print(type(data_convertida))
    nova_data = data_convertida + timedelta(days=365)
    nova_data = nova_data.strftime('%d/%m/%Y')
    print(nova_data)
    #nova_data = datetime.now() + timedelta(days=365)
    #nova_data = nova_data.strftime('%d/%m/%Y')
    #print(nova_data)

if __name__ == '__main__':
    somando_data('07/05/2020')
    #trabalhando_com_timedelta()
    #trabalhando_com_date()
    #trabalhando_com_time()
    #trabalhando_com_datetime()