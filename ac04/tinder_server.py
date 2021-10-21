from flask import Flask, jsonify, request
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
    i.append(dicionario_pessoa)
    return jsonify({"status":"ok"})

@app.route("/pessoas/<int:id_pessoa>")
def pessoa_por_id(id_pessoa):
    pessoa = i.localiza_pessoa(id_pessoa)
    return jsonify(pessoa)

