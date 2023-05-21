from flask import Flask, jsonify, request
import mysql.connector
import sys, json
sys.path.append('C:/Users/pedro/reactstudies/')
from reactapp01 import db_pass

app = Flask(__name__)

bd = mysql.connector.connect(host='localhost', user='root', password=db_pass.PASSWORD, database='db_alunos')

@app.route('/listar', methods=['GET'])
def listarAlunos():
    selectAllSql = f"SELECT * FROM tb_aluno"
    cursor = bd.cursor()
    cursor.execute(selectAllSql)
    resultado = cursor.fetchall()
    return jsonify(resultado)

@app.route('/incluir', methods=['POST'])
def incluirAlunos():
    data = json.loads(request.data)
    nome = data.get('nome', None)
    turma = data.get('turma', None)
    disciplina = data.get('disciplina', None)
    query = f"INSERT INTO tb_aluno (nome, turma, disciplina) VALUES (%s, %s, %s)"
    val = (nome, turma, disciplina)
    cursor = bd.cursor()
    cursor.execute(query, val)
    bd.commit()
    bd.close()
    cursor.close()
    return f"Aluno {nome} inserido com sucesso."

if __name__ == '__main__':
    app.run(debug=True)