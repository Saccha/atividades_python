from flask import Flask, jsonify, request
import estrutura_interesses as i

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/pessoas")
def listar_pessoas():
    lista = i.todas_as_pessoas()
    return jsonify(lista)



