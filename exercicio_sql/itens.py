import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')

class ItemNaoExisteException(Exception):
    pass

'''
Ex3
O arquivo itens.py
deve conter uma funcao consultar_item.
ela recebe uma id de item e retorna 
um dicionario com todos os dados do item
(por exemplo, a chave 'nome' conterá o valor
da coluna 'nome' associada a essa id).

se receber uma id invalida, a funcao levanta 
uma ItemNaoExisteException (que voce deverá
criar)

(já fizemos coisa parecida no heroi. Lá, foram
3 testes, agora é um só testando tudo!)
'''

def item_existe(id):
    with engine.connect() as conexao:
        sql = f'SELECT * FROM Item WHERE id = {id}'
        resultado = conexao.execute(sql, id=id)
        item = resultado.fetchone() # Pegando a primeira linha.
        return False if item is None else True

def consultar_item(id):
    if item_existe(id):
        with engine.connect() as conexao:
            sql = f'SELECT * FROM Item WHERE id = {id}'
            resultado = conexao.execute(sql, id=id)
            item = resultado.fetchone() # Pegando a primeira linha.
            return False if id is None else dict(item)
    else:
        raise ItemNaoExisteException

