from Analyzer.Gramatica import parser
from AnalyzerC3D.Gramatica import parser2
from Mirilla import Mirilla
'''from flask import Flask, request
from flask_cors import CORS
from Globales.Tablas import GraficaError
from Globales.Tablas import GraficaTS
from Globales.Tablas import GraficaTO
from Globales.Tablas import Errores
from Globales.Tablas import Simbolos
from Globales.Tablas import Optimizacion

app = Flask(__name__)
CORS(app)


@app.route('/ping')
def prueba():
    return 'MACARIO JOTO'


@app.route('/Analizador', methods=['POST'])
def Analizar():
    C3D = parser.parse(request.json['Texto'])
    data = {'Salida': C3D, 'TO': GraficaTO(Optimizacion), 'TS': GraficaTS(Simbolos), 'TE': GraficaError(Errores)}
    Errores.clear()
    Simbolos.clear()
    Optimizacion.clear()
    return data


if __name__ == '__main__':
    app.run(threaded=True, debug=True, port=4000)
    app.run(threaded=True, debug=True, port="https://back2compi.herokuapp.com")'''

'''f = open("./entrada.txt", "r")
entrada = f.read()
C3D = parser.parse(entrada)

f2 = open("./salida.txt", "w")
f2.write(C3D)'''

f3 = open("./salida.txt", "r")
entrada2 = f3.read()
C3DOM = parser2.parse(entrada2)

mirilla: Mirilla = Mirilla()
C3DOM_1 = mirilla.rule1(C3DOM)
C3DOM_2 = mirilla.rule2(C3DOM_1)

outText = ""
for ins in C3DOM_2:
    if ins.write:
        outText = outText + ins.writeC3D() + "\n"

f4 = open("salida2.txt", "w")
f4.write(outText)
