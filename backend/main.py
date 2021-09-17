from Analyzer.Gramatica import parser
from Arbol.GramaticaArbol import parser2
from flask import Flask, request
from flask_cors import CORS
from Globales.Arbol import contenido
from Globales.Tablas import GraficaError
from Globales.Tablas import GraficaTS
from Globales.Tablas import Errores
from Globales.Tablas import Simbolos

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
        tmp = valor.split(sep=",", maxsplit=1)
        if tmp[0] == "P":
            salida = salida + tmp[1]
        else:
            salida = salida + tmp[1] + "\n"
    parser2.parse(request.json['Texto'])
    f = open("./salida.txt", "r")
    data = {'Salida': salida, 'Dot': f.read(), 'TS': GraficaTS(Simbolos), 'TE': GraficaError(Errores)}
    contenido.clear()
    Errores.clear()
    Simbolos.clear()
    return data


if __name__ == '__main__':
    '''app.run(threaded=True, debug=True, port=4000)'''
    app.run(threaded=True, debug=True, port="https://backcompi.herokuapp.com")


'''f = open("./entrada.txt", "r")
input = f.read()
parser2.parse(input)
TS = GraficaTS(Simbolos)
TE = GraficaError(Errores)
salida = ""'''
