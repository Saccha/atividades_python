from flask import request, jsonify, Flask
app = Flask(__name__)

dados = {
    'alunos': [
        {"nome": 'Fulano', 'id': 100},
        {"nome": 'Ciclano', 'id': 101}
    ],
    'professores': []
}

aluno = {"nome": 'Beltrano', 'id': 12}
dados['alunos'].append(aluno)


@app.route("/")
def hello():
    return "Controle de Usuários"


@app.route('/alunos')
def alunos():
    return jsonify(dados['alunos'])

@app.route("/alunos", methods=['GET']) #espeficiquei o verbo. Como era GET nao precisava, mas eu quis
def get_alunos():
    #return dados["alunos"] #esse return dá problema. O flask basicamente espera uma string ou um dict
    return jsonify(dados["alunos"])

@app.route("/alunos", methods=['POST']) #espeficiquei o verbo.
def post_alunos():
    dic_que_o_cliente_enviou = request.json
    dados['alunos'].append(dic_que_o_cliente_enviou)
    return jsonify(dados["alunos"])

@app.route("/alunos/<int:id_aluno>", methods=["DELETE"])
def deleta(id_aluno):
    for i in range(len(dados['alunos'])):
        if(id_aluno == dados['alunos'][i]['id']):
            dados['alunos'].pop(i)
            return jsonify({"status":"ok"}),201
    return jsonify({'erro': 'aluno nao encontrado'}), 404

@app.route("/alunos/<int:id_aluno>", methods=["PUT"])
def edita(id_aluno):
    dicionario_recebido = request.json
    if ('nome' in dicionario_recebido.keys()):
        for i in range(len(dados['alunos'])):
            if(id_aluno == dados['alunos'][i]['id']):
                dados['alunos'][i]['nome'] = dicionario_recebido['nome']
                return jsonify({"status":"ok"}),201    
        return jsonify({'erro': 'aluno nao encontrado'}), 404
    else:
        return jsonify({'erro': 'aluno sem nome'}), 400

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------- PROFESSORES -------------------------------------
# ------------------------------------------------------------------------------------------------------------

@app.route('/professores')
def professores():
    return jsonify(dados['professores'])

@app.route('/professores', methods=['POST'])
def cria_professor():
    dicionario_recebido = request.json
    temp = []
    for i in range(len(dados['professores'])):
        temp.append(dados['professores'][i]['id'])
    if (dicionario_recebido['id'] in temp):
        return jsonify({'erro': 'id ja utilizada'}), 400
    elif ('nome' not in dicionario_recebido.keys()):
        return jsonify({'erro': 'professor sem nome'}), 400
    else: 
        dados['professores'].append(dicionario_recebido)
        return jsonify(dados['professores'])
   

@app.route('/professores/<int:id_professor>')
def professor_por_id(id_professor):
    lista_professores = dados['professores']
    for professor in lista_professores:
        if id_professor == professor['id']:
            return jsonify(professor)
    return jsonify({'erro': 'professor nao encontrado'}), 400

@app.route("/professores/<int:id_professor>", methods=["DELETE"])
def deleta_professor(id_professor):
    for i in range(len(dados['professores'])):
        if(id_professor == dados['professores'][i]['id']):
            dados['professores'].pop(i)
            return jsonify({"status":"ok"}),201
    return jsonify({'erro': 'professor nao encontrado'}), 400

@app.route("/professores/<int:id_professor>", methods=["PUT"])
def edita_professor(id_professor):
    dicionario_recebido = request.json
    if ('nome' in dicionario_recebido.keys()):
        for i in range(len(dados['professores'])):
            if(id_professor == dados['professores'][i]['id']):
                dados['professores'][i]['nome'] = dicionario_recebido['nome']
                return jsonify({"status":"ok"}),201    
        return jsonify({'erro': 'professor nao encontrado'}), 400
    else:
        return jsonify({'erro': 'professor sem nome'}), 400  

@app.route('/reseta', methods=['POST'])
def reseta():
    lista_alunos = dados['alunos']
    lista_professores = dados['professores']
    lista_alunos.clear()
    lista_professores.clear()
    return jsonify(),200

if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)