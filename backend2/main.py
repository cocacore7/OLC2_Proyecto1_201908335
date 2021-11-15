from flask import Flask, request
from flask_cors import CORS

from Analyzer.Gramatica import parser
from AnalyzerC3D.GramaticaC3D import parser2
from Mirilla import Mirilla
from Bloques import Bloques

from Globales.Tablas import GraficaTS
from Globales.Tablas import GraficaError

from Globales.Tablas import Optimizacion
from Globales.Tablas import Simbolos
from Globales.Tablas import Errores

app = Flask(__name__)
CORS(app)


@app.route('/ping')
def prueba():
    return 'MACARIO JOTO'


@app.route('/Compilador', methods=['POST'])
def Compilar():
    Codigo = parser.parse(request.json['Texto'])
    Filas = {'Filas': []}
    for i in Optimizacion:
        Filas['Filas'].append(
            {
                'Tipo': i["Tipo"],
                'Regla': i["Regla"],
                'ExpOr': i["ExpOr"],
                'ExpOp': i["ExpOp"],
                'Fila': i["Fila"]
            }
        )
    data = {'Salida': Codigo, 'TO': Filas, 'TS': GraficaTS(Simbolos), 'TE': GraficaError(Errores)}
    Errores.clear()
    Simbolos.clear()

    Optimizacion.clear()
    return data


@app.route('/OptimizadorMirilla', methods=['POST'])
def OptimizarM():
    C3D = parser2.parse(request.json['Texto'])
    mirilla: Mirilla = Mirilla()
    C3DOM_1 = mirilla.rule1(C3D)
    C3DOM_2 = mirilla.rule2(C3DOM_1)
    C3DOM_3 = mirilla.rule3(C3DOM_2)
    C3DOM_6 = mirilla.rule6(C3DOM_3)
    C3DOM_7 = mirilla.rule7(C3DOM_6)
    C3DOM_8 = mirilla.rule8(C3DOM_7)
    outText = ""
    for ins in C3DOM_8:
        if ins.write:
            outText = outText + ins.writeC3D() + "\n"

    Filas = {'Filas': []}
    for i in Optimizacion:
        Filas['Filas'].append(
            {
                'Tipo': i["Tipo"],
                'Regla': i["Regla"],
                'ExpOr': i["ExpOr"],
                'ExpOp': i["ExpOp"],
                'Fila': i["Fila"]
            }
        )
    data = {'Salida': outText, 'TO': Filas}
    Optimizacion.clear()
    return data


@app.route('/OptimizadorBloques', methods=['POST'])
def OptimizarB():
    # C3D = parser2.parse(request.json['Texto'])
    Filas = {'Filas': []}
    for i in Optimizacion:
        Filas['Filas'].append(
            {
                'Tipo': i["Tipo"],
                'Regla': i["Regla"],
                'ExpOr': i["ExpOr"],
                'ExpOp': i["ExpOp"],
                'Fila': i["Fila"]
            }
        )
    data = {'Salida': request.json['Texto'], 'TO': Filas}
    Optimizacion.clear()
    return data


if __name__ == '__main__':
    app.run(threaded=True, debug=True, port=4000)
