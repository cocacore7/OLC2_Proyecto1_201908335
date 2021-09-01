from Analyzer.Panther import parser
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/ping')
def prueba():
    return 'MACARIO JOTO'

@app.route('/Analizador', methods=['POST'])
def Analizar():
    print(request.json['Texto'])
    parser.parse(request.json['Texto'])
    return 'Entrada Recibida'


if __name__ == '__main__':
    app.run(threaded=True,debug=True, port=4000)
