from Analyzer.Gramatica import parser
from flask import Flask, request
from flask_cors import CORS
from Salida import contenido

app = Flask(__name__)
CORS(app)


@app.route('/ping')
def prueba():
    return 'MACARIO JOTO'


@app.route('/Analizador', methods=['POST'])
def Analizar():
    parser.parse(request.json['Texto'])
    salida = ""
    for valor in contenido:
        salida = salida + valor + "\n"
    print(contenido)
    contenido.clear()
    return salida


if __name__ == '__main__':
    app.run(threaded=True, debug=True, port=4000)
