from sqlalchemy import create_engine
from sqlalchemy.sql import text
 
engine = create_engine('sqlite:///rpg.db')
 
# Essa classe só representa uma exception com
#novo nome. Não mexa dentro dela.
# Escreva os imports (acima dela)
# E suas funcoes (depois dela)
class HeroiNaoExisteException(Exception):
   pass

'''
Ex1
O arquivo herois deve conter uma função heroi_existe
Ela recebe uma id de herói e consulta no banco para ver
se o herói em questão existe. Ela retorna True
se ele existe, False caso contrário
'''
 
def heroi_existe(id_h):
   with engine.connect() as con: #gerei uma variavel con que representa uma conexao
                                 #no banco de dados. Con.execute vai me permitir rodar
                                 #uma query
                                 #Pode imaginar que seja con = engine.connect()
       statement = text ("""SELECT * FROM heroi WHERE id = :heroi""")
       #defini  uma string que representa uma consulta no banco de dados. Deixei
       #um buraco pra colocar a id do heroi
 
       rs = con.execute(statement, heroi=id_h)
       #banco de dados, execute a query, preenchendo o buraco
       # a query tinha um buraco :heroi
       # execute recebeu um argumento chamado heroi "rs [...] heroi=id_h)"
 
 
       heroi = rs.fetchone()
       #eu fiz essa consulta, e ela (espero!) retornou linhas
       #estou pedindo pra ele pegar a primeira linha
       #se havia alguma linha, recebo um objeto que a representa,
       # uma coisa conversível em tupla ou dicionário
       #se nao havia nenhuma, se a query nao retornou nada, se o heroi nao
       #existia, essa funcao retornou None
 
       if heroi == None: #se ela retornou None, o heroi nao existe, False                     
           return False
       return True

'''
Ex2
O arquivo herois deve conter uma funcao 
consultar_heroi.
ela recebe uma id de heroi e retorna 
um dicionario com todos os dados do heroi
(por exemplo, a chave 'nome' conterá o valor
da coluna 'nome' associada a essa id).

se receber uma id invalida, a funcao levanta 
uma HeroiNaoExisteException 
'''
def consultar_heroi(id):
    if heroi_existe(id):
        with engine.connect() as conexao:
            sql = f'SELECT * FROM Heroi WHERE id = {id}'
            resultado = conexao.execute(sql, id=id)
            heroi = resultado.fetchone()
            return False if heroi is None else dict(heroi)
    else:
        raise HeroiNaoExisteException

