from Analyzer.Gramatica import parser
from flask import Flask, request
from flask_cors import CORS
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
    C3D = parser.parse(request.json['Texto'])
    data = {'Salida': C3D, 'Dot': C3D, 'TS': GraficaTS(Simbolos), 'TE': GraficaError(Errores)}
    Errores.clear()
    Simbolos.clear()
    return data


if __name__ == '__main__':
    app.run(threaded=True, debug=True, port=4000)
    '''app.run(threaded=True, debug=True, port="https://back2compi.herokuapp.com")'''

'''f = open("./entrada.txt", "r")
entrada = f.read()
C3D = parser.parse(entrada)

f2 = open("./salida.txt", "w")
f2.write(C3D)'''
