import requests
from flask import Flask, redirect, url_for, request, Response


from controller.GrupoController import GrupoController
from controller.UsuarioController import UsuarioController
from controller.TarefaController import TarefaController
from controller.GrupoHasUsuarioController import GrupoHasUsuarioController

import json
app = Flask(__name__)

# @app.route('/')
# def root():
#     return json.dumps()

master_ip = None
ips = None
my_ip = "192.168.1.4"

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
    GrupoHasUsuarioController().entrarGrupo(dados["usuario_id"], dados["grupo_id"], dados["eh_administrador"])
    response =  Response(json.dumps(request.form), status=200, mimetype='application/json')
    return response
    

@app.route('/ping_master', methods = ["GET"])
def pingMaster():
    response =  Response(json.dumps(master_ip), status=200, mimetype='application/json')
    return response

if __name__ == '__main__':
    with open("ip-config.txt", "r") as arquivo:
        ips = arquivo.read().strip().splitlines()
        print(ips)

    for ip in ips:
        if(ip != my_ip):
            route_ping = "http://" + str(ip) + "/ping_master"
            try:
                response = requests.get(route_ping)
                if(response.status == 200):
                    master_ip = ip
                else:
                    master_ip = my_ip
            except:
                master_ip = my_ip
    print(master_ip)
    print(my_ip)
    print(ips)

    app.run(debug = True)