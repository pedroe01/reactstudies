from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/flaskapi', methods=['GET'])
def flask_api():
    return jsonify([{
        'disciplina': 'Frameworks FullStack',
        'atividade': 'AC3',
        'aluno': 'Pedro Egydio da Silva Faria',
        'turma': 'SI4A',
        'ra': '2102057'
    }])

if __name__ == '__main__':
    app.run(debug=True)