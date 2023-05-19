from flask import Flask, jsonify, request
import mysql.connector
import sys
sys.path.append('C:/Users/pedro/reactstudies/')
from reactapp01 import db_pass

app = Flask(__name__)

bd = mysql.connector.connect(host='localhost', user='root', password=db_pass.PASSWORD, database='db_alunos')

@app.route('/listar', methods=['GET'])
def listarAlunos():
    selectAllSql = f"select * from tb_aluno"
    cursor = bd.cursor()
    cursor.execute(selectAllSql)
    resultado = cursor.fetchall()
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)