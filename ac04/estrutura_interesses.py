database = {} #um dicionário, que tem a chave interesses para o controle
#dos interesses (que pessoa se interessa por que outra), e pessoas para o controle de pessoas (quem sao as pessoas e quais sao os dados pessoais de cada pessoa no sistema)
#voce pode controlar as pessoas de outra forma se quiser, nao precisa mudar nada
#do seu código para usar essa váriavel

database['PESSOA'] = [{"nome":"pateta", 'id': 123},{"nome":"mickey", 'id': 124}] #esse voce só faz se quiser guardar nessa lista os dicionários das pessoas

#em todo esse codigo que estou compartilhando, as variaveis interessado, alvo de interesse, pessoa, pessoa1 e pessoa2 sao sempre IDs de pessoas

class NotFoundError(Exception):
    pass

# Assim, poderemos adicionar pessoas: i.adiciona_pessoa({'nome':'fernando','id':1})
# Pegar a lista de todas as pessoas : i.todas_as_pessoas()
# Consultar uma pessoa por id       : i.localiza_pessoa(1) (retorna o dicionario do fernando)

# Tb queremos uma função reseta.    : i.reseta() faz a lista de pessoas ficar vazia

def todas_as_pessoas():
    return database['PESSOA']

def adiciona_pessoa(dic_pessoa): #dic pessoa vai ser {"nome": "margarida", "id": 134}
    #TODO e se eu adicionar uma segunda pessoa com a mesma id??
    lista_pessoas = database['PESSOA']
    lista_pessoas.append(dic_pessoa)
    id_pessoa = dic_pessoa['id']
    database['interesses'][id_pessoa] = []

def localiza_pessoa(id_pessoa):
    for dic_pessoa in database['PESSOA']:
        if dic_pessoa['id'] == id_pessoa:
            return dic_pessoa
    raise NotFoundError

def reseta():
    database['PESSOA'] = []

database['interesses'] = { 
    100: [101, 102, 103],
    200: [100]
}

class IncompatibleError(Exception):
    pass
    maximus = {'nome':'maximus','id':9,'sexo':'homem','buscando':['mulher','homem']}
    scipio  = {'nome':'scipio','id':10,'sexo':'homem','buscando':['mulher']}
    #se o 9 manifesta interesse no 10, verifico que o sexo do 10 é compativel com o buscando do 9
def adiciona_interesse(id_interessado, id_alvo_de_interesse):
    d_interessado = localiza_pessoa(id_interessado)  #se essa funcao lancar uma exception, eu fiz try, eu explodo junto
    d_alvo        = localiza_pessoa(id_alvo_de_interesse)
    if 'sexo' in d_alvo and 'buscando' in d_interessado:
        if d_alvo['sexo'] not in d_interessado['buscando']:
            raise IncompatibleError
    database['interesses'][id_interessado].append(id_alvo_de_interesse)


def consulta_interesses(id_interessado):
    localiza_pessoa(id_interessado)  #se essa funcao lancar uma exception, eu fiz try, eu explodo junto
    return database['interesses'][id_interessado]

def remove_interesse(id_interessado,id_alvo_de_interesse):
    localiza_pessoa(id_interessado)  #se essa funcao lancar uma exception, eu fiz try, eu explodo junto
    localiza_pessoa(id_alvo_de_interesse)
    lista_do_interessado = consulta_interesses(id_interessado)
    if id_alvo_de_interesse in lista_do_interessado:
        lista_do_interessado.remove(id_alvo_de_interesse)


#te passo 2 ids, você diz True se é match, False, caso contrário
def verifica_match(id1,id2):
    lista1 = consulta_interesses(id1)
    lista2 = consulta_interesses(id2)
    p1_gosta_de_p2 = id2 in lista1
    p2_gosta_de_p1 = id1 in lista2
    if p1_gosta_de_p2 and p2_gosta_de_p1:
        return True
    else:
        return False


#construir essa sem chamar a de cima
# TODO como passou       test_p3_01_match_com_pessoas_invalidas (__main__.TestStringMethods) ... ok ?????
database['interesses'] = { 
    100: [101, 102, 103],
    200: [100]
}
def lista_matches(id_pessoa): #100
    lista = consulta_interesses(id_pessoa) #[101, 102, 103]
    matches = []
    for outro in lista: #101
        l_outro = consulta_interesses(outro)
        #if verifica_match(outro,id_pessoa):
        if id_pessoa in l_outro:
            matches.append(outro)
    return matches