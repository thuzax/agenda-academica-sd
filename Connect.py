import socket
import requests
import sys
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
my_ip = ""

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

def getMyIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def getMasterIp():
    for ip in ips:
        if(ip != my_ip):
            print(ip)
            route_ping = "http://" + str(ip) + ":5000" + "/ping_master"
            print(route_ping)
            try:
                response = requests.get(route_ping)
                if(response.status_code == 200):
                    return ip
            except:
                continue

    return my_ip

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("Deve ser passado por parametro o id do servidor")
        return
    id_maquina = sys.argv[1]
    my_ip = getMyIp()
    print("meu IP: ", my_ip )
    with open("ip-config.txt", "r") as arquivo:
        ips = arquivo.read().strip().splitlines()
        print(ips)
        
    master_ip = getMasterIp()
    
    print("master: ",master_ip)
    print("meu ip: ",my_ip)
    print("todos: ", ips)

    with open("banco-de-dados/mysqld.cnf", "r") as arquivo:
        saida = arquivo.read()
    
    saida += id_maquina
    with open("/etc/mysql/mysql.conf.d/mysqld.cnf", "w") as arquivo:
        pass

    app.run(debug = True, host = "0.0.0.0")
