from flask import Flask, jsonify, request, json
import estrutura_interesses as i

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/pessoas")
def listar_pessoas():
    lista = i.todas_as_pessoas()
    return jsonify(lista)

@app.route("/pessoas", methods=["POST"])
def add_pessoa():
    dicionario_pessoa = request.json
    i.adiciona_pessoa(dicionario_pessoa)
    return jsonify({"status":"ok"},200)

@app.route("/pessoas/<int:id_pessoa>")
def pessoa_por_id(id_pessoa):
    pessoa = i.localiza_pessoa(id_pessoa)
    return jsonify(pessoa)

@app.route("/reseta", methods=['POST'])
def reseta():
    i.reseta()
    return jsonify({"status":"ok"})

@app.route("/interesses/<int:id_pessoa>")
def pega_interesses(id_pessoa):
    try:
        interesses = i.consulta_interesses(id_pessoa)
    except i.NotFoundError:
        return jsonify({"erro":"usuário inválido"}),404
    return jsonify(interesses)

@app.route("/sinalizar_interesse/<int:id_pessoa>/<int:id_interesse>/", methods=['PUT'])
def sinalizar_interesse(id_pessoa, id_interesse):
    try:
        i.adiciona_interesse(id_pessoa, id_interesse)
    except i.NotFoundError:
        return jsonify({"erro":"usuário inválido"}),404
    except i.IncompatibleError:
        return jsonify({"erro":"interesse incompativel"}),400
    interesses = i.consulta_interesses(id_pessoa)
    return jsonify(interesses)

@app.route("/sinalizar_interesse/<int:id_pessoa>/<int:id_interesse>/", methods=['DELETE'])
def remover_interesse(id_pessoa, id_interesse):
    try:
        i.remove_interesse(id_pessoa, id_interesse)
    except i.NotFoundError:
        return jsonify({"erro":"usuário inválido"}),404
    interesses = i.consulta_interesses(id_pessoa)
    return jsonify(interesses)

@app.route("/matches/<int:id_pessoa>", methods=['GET'])
def matches(id_pessoa):
    try:
        matches = i.lista_matches(id_pessoa)
    except i.NotFoundError:
        return jsonify({"erro":"usuário inválido"}),404
    return jsonify(matches)

if __name__ == '__main__':     
   app.run(host = 'localhost', port = 5003, debug=True)



