from sqlalchemy import create_engine
from sqlalchemy.sql import text

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

def consultar_item(id_item):
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()

    sql = "SELECT * FROM Item WHERE id = (?)"
    cursor.execute(sql, [id_item])

    item = cursor.fetchone()
    if item is None:
        raise ItemNaoExisteException

    connection.close()
    item = {
        'id': item[0],
        'nome': item[1],
        'tipo': item[2],
        'fisico': item[3],
        'magia': item[4],
        'agilidade': item[5],
        'emUso': item[6]
    }
    return item

