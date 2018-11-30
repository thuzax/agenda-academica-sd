from flask import Flask, redirect, url_for, request, Response

from controller.GrupoController import GrupoController
from controller.UsuarioController import UsuarioController
from controller.TarefaController import TarefaController

import json
app = Flask(__name__)

# @app.route('/')
# def root():
#     return json.dumps()

@app.route('/adicionar/usuario',methods = ['POST'])
def adicionarUsuario():
    dados = request.form
    UsuarioController().adicionarUsuario(dados["nome"], dados["login"], dados["senha"])
    response = Response(json.dumps(request.form), status=200, mimetype='application/json')
    return response
        
    
@app.route('/adicionar/grupo',methods = ['POST'])
def adicionarGrupo():
    dados = request.form
    GrupoController().adicionarGrupo(dados["nome"])
    response = Response(json.dumps(request.form), status=200, mimetype='application/json')
    return response

@app.route('/adicionar/tarefa',methods = ['POST'])
def adicionarTarefa():
    dados = request.form
    TarefaController().adicionarTarefa(dados["data"], dados["horario"], dados["titulo"], dados["descricao"], dados["dono_id"])
    response = Response(json.dumps(request.form), status=200, mimetype='application/json')
    return response

@app.route('/entrar_grupo', methods = ["POST"])
def entrarGrupo():
    dados = request.form
    print(dados["usuario_id"], dados["grupo_id"], dados["eh_administrador"])
    response = Response(json.dumps(request.form), status=200, mimetype='application/json')
    return response
    

if __name__ == '__main__':
   app.run(debug = True)