from Analyzer.Gramatica import parser
'''from flask import Flask, request
from flask_cors import CORS
from Globales.Salida import contenido

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
        tmp = valor.split(sep=",",maxsplit=2)
        if tmp[0] == "P":
            salida = salida + tmp[1]
        else:
            salida = salida + tmp[1] + "\n"
    contenido.clear()
    return salida


if __name__ == '__main__':
    app.run(threaded=True, debug=True, port=4000)
'''
f = open("./entrada.txt", "r")
input = f.read()
parser.parse(input)