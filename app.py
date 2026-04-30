#import do flask para criação do servidor
#render_template para criar uma "ponte"com html
#request para capturar os dados digitados

from flask import Flask, render_template, request
import mysql.connector

#ajuda o Flask a localizar os caminhos dos arquivos
app = Flask(__name__)

bd_config = {
   #'chave' : 'valor'
     'host' : 'localhost', #se externo usar a URL do servidor
     'user' : 'root',
     'password' : 'escola',
     'database' : 'cadastro'
}
#print (type (bd_config)) para listar referencias do DB
#criando uma rota
@app.route('/')
def index():
    return render_template('index.html')
#criando rota para acessar o formulário
@app.route('/cadastrar', methods=['post'])
def cadastrar():
    cpf = request.form['cpf']
    primeiro_nome = request.form['primeiro_nome']
    sobrenome = request.form['sobrenome']
    idade = request.form['idade']

    try:
        #verificando conexão com MYSQL
        conectar = mysql.connector.connect(**bd_config)
        #variável que permite a escrever SQL
        cursor = conectar.cursor()

        query = "INSERT INTO cliente(CPF,PRIMEIRO_NOME,SOBRENOME,IDADE) VALUES (%s,%s,%s,%s)"
        cursor.execute(query,(cpf,primeiro_nome,sobrenome,idade))

        #Atuliza as alterações e fecha as conexões
        conectar.commit()
        cursor.close()
        conectar.close()
       
        return f"<h3>Cliente {primeiro_nome} salvo com sucesso!</h3>"
    
    except mysql.connector.Error as err:
        return f"Erro ao gravar no banco: {err}"

if __name__ ==' __main__ ':
    app.run(debug=True)
    