import requests

def retorna_dados_cep(cep):
    #fazendo uma requisição
    #response = requests.get('https://viacep.com.br/ws/01001000/json')
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    #verificando o retorno = 200 foi ok se for 400 não exist
    print(response.status_code)
    #exibindo como string
    print(response.text)
    print(type(response.text))
    #exibindo como dicionario
    print(response.json())
    print(type(response.json()))
    #para pegar e exibir uma determinada informação
    dados_cep = response.json()
    #iremos exibindo as informações de logradouro
    print(dados_cep['logradouro'])
    #iremos exibindo as informações de complemento
    print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://www.google.com/')
    print(response)
    #retorna_dados_cep('22041001')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon['sprites']['front_shiny'])