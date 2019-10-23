from flask import Flask, request

from controllers.Indicadores import Indicador

app = Flask(__name__)


@app.route('/indicadores', methods=['GET'])
def getAll():
    return (Indicador.listar())

@app.route('/indicadores', methods=['POST'])
def postOne():
    body = request.json
    return (Indicador.crear(body))

app.run(port=5000, debug=True)
