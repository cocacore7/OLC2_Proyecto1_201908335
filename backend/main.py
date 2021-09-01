from Analyzer.Panther import parser
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/Analizador', methods=['POST'])
def Analizar():
    print(request.json['Texto'])
    parser.parse(request.json['Texto'])
    return 'Entrada Recibida'


if __name__ == '__main__':
    app.run(debug=True, port=4000)
