from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tarefas para armazenar as tarefas
tarefas = []

# Página inicial, exibe as tarefas e o formulário para adicionar novas
@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

# Rota para adicionar uma nova tarefa
@app.route('/adicionar', methods=['POST'])
def adicionar():
    tarefa = request.form['tarefa']  # Obtém a tarefa enviada pelo formulário
    if tarefa:
        tarefas.append(tarefa)  # Adiciona a tarefa à lista
    return redirect(url_for('index'))  # Redireciona para a página inicial

# Rota para remover uma tarefa
@app.route('/remover/<int:tarefa_id>')
def remover(tarefa_id):
    if 0 <= tarefa_id < len(tarefas):
        del tarefas[tarefa_id]  # Remove a tarefa com o índice fornecido
    return redirect(url_for('index'))  # Redireciona para a página inicial

if __name__ == '__main__':
    app.run(debug=True)
