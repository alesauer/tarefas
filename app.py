from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tarefas (simulação de banco de dados)
tarefas = []

@app.route('/')
def index():
    #Exibe a página principal com a lista de tarefas
    return render_template('index.html', tarefas=tarefas)

@app.route("/add",methods=['POST'])    
def add():
    tarefa = request.form['tarefa']
    tarefas.append(tarefa)
    return redirect(url_for('index'))

@app.route("/delete", methods=['POST'])
def delete():
    pass




app.run(debug=True)
