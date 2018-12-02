import socket
import requests
import sys
import json
import os
from flask import Flask, redirect, url_for, request, Response, jsonify


from controller.GrupoController import GrupoController
from controller.UsuarioController import UsuarioController
from controller.TarefaController import TarefaController
from controller.GrupoHasUsuarioController import GrupoHasUsuarioController

from Gerenciador import Gerenciador

import json
app = Flask(__name__)

# @app.route('/')
# def root():
#     return json.dumps()

gerenciador = Gerenciador()

@app.route('/adicionar/usuario',methods = ['POST'])
def adicionarUsuario():
    dados = getJsonFromRequest(request)
    usuario_id = UsuarioController().adicionarUsuario(dados["nome"], dados["login"], dados["senha"])
    response = Response(json.dumps({"usuario_id" : usuario_id}), status=200, mimetype='application/json')
    return response
        
    
@app.route('/adicionar/grupo',methods = ['POST'])
def adicionarGrupo():
    dados = getJsonFromRequest(request)
    GrupoController().adicionarGrupo(dados["nome"])
    response = Response(json.dumps(dados), status=200, mimetype='application/json')
    return response

@app.route('/adicionar/tarefa',methods = ['POST'])
def adicionarTarefa():
    dados = getJsonFromRequest(request)
    TarefaController().adicionarTarefa(dados["data"], dados["horario"], dados["titulo"], dados["descricao"], dados["dono_id"])
    response = Response(json.dumps(dados), status=200, mimetype='application/json')
    return response

@app.route('/entrar_grupo', methods = ["POST"])
def entrarGrupo():
    dados = getJsonFromRequest(request)
    GrupoHasUsuarioController().entrarGrupo(dados["usuario_id"], dados["grupo_id"], dados["eh_administrador"])
    response =  Response(json.dumps(dados), status=200, mimetype='application/json')
    return response
    

@app.route('/buscar/tarefas/dono', methods = ["GET"])
def buscarTarefaDono():
    dados = getJsonFromRequest(request)
    tarefas = TarefaController().buscarTarefasDono(dados["dono_id"])
    response =  Response(json.dumps(tarefas), status=200, mimetype='application/json')
    return response

@app.route('/buscar/tarefas/data', methods = ["GET"])
def buscarTarefasData():
    dados = getJsonFromRequest(request)
    print(dados)
    tarefas = TarefaController().buscarTarefasData(dados["dono_id"], dados["data"])
    print(tarefas)
    response =  Response(json.dumps(tarefas), status=200, mimetype='application/json')
    return response


@app.route('/buscar/grupos/id_ou_user', methods = ["GET"])
def buscarGrupos():
    dados = getJsonFromRequest(request)
    grupos = GrupoController().buscarGrupos(dados["grupo_id"], dados["usuario_id"])
    response =  Response(json.dumps(grupos), status=200, mimetype='application/json')
    return response

@app.route('/login', methods = ["POST"])
def login():
    dados = getJsonFromRequest(request)
    usuario_id = UsuarioController().login(dados["login"], dados["senha"])
    response = Response(json.dumps({"usuario_id" : usuario_id}), status=200, mimetype='application/json')
    return response


@app.route('/sair_grupo', methods = ["POST"])
def sairGrupo():
    dados = getJsonFromRequest(request)
    GrupoHasUsuarioController().sair(dados["usuario_id"], dados["grupo_id"])
    response = Response(json.dumps({"mensagem" : "ok"}), status=200, mimetype='application/json')
    return response


@app.route('/buscar/grupos/participante', methods = ["GET"])
def buscarGruposParticipante():
    dados = getJsonFromRequest(request)
    grupos_participante = GrupoHasUsuarioController().buscarGruposParticipante(dados["usuario_id"])
    response = Response(json.dumps(grupos_participante), status=200, mimetype='application/json')
    return response



@app.route('/ping_master', methods = ["GET"])
def pingMaster():
    response =  Response(json.dumps(master_ip), status=200, mimetype='application/json')
    return response


def getJsonFromRequest(request):
    dados = request.get_json()
    json_acceptable_string = dados.replace("'", "\"")
    dados = json.loads(json_acceptable_string)
    return dados

def getMyIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def getMasterIp(ips, my_ip):
    print(ips)
    for ip in ips:
        if(ip != my_ip):
            print(ip)
            route_ping = "http://" + str(ip) + ":5000" + "/ping_master"
            print(route_ping)
            try:
                response = requests.get(route_ping, timeout = 1)
                if(response.status_code == 200):
                    return ip
            except:
                continue

    return my_ip

def main(gereciador):
    if(len(sys.argv) < 2):
        print("Deve ser passado por parametro o id do servidor")
        return
    gerenciador.id_maquina = sys.argv[1]
    gerenciador.my_ip = getMyIp()
    print("meu IP: ", gerenciador.my_ip)
    with open("ip-config.txt", "r") as arquivo:
        ips = arquivo.read().strip().splitlines()
    print(ips)
    
    gerenciador.ips = ips

    gerenciador.master_ip = getMasterIp(gereciador.ips, gereciador.my_ip)
    
    print("master: ", gerenciador.master_ip)
    print("meu ip: ", gerenciador.my_ip)
    print("todos: ", gerenciador.ips)

    texto_novo = ""
    with open("banco-de-dados/mysqld.cnf", "r") as arquivo:
        entrada = arquivo.read().strip().splitlines()
        list_novo = []
        for linha in entrada:
            list_linha = linha.strip().split()
            list_nova_linha = []
            
            i = 0
            while(i < len(list_linha)):
                if(list_linha[i] == "bind-address"):
                    if(list_linha[i + 1] == "="):
                        if(list_linha[i + 2] == "127.0.0.1"):
                            list_nova_linha.append(list_linha[i])
                            list_nova_linha.append(list_linha[i + 1])
                            list_nova_linha.append("0.0.0.0")
                            i += 3
                            continue
                list_nova_linha.append(list_linha[i])
                i += 1
            
            frase = ""
            for palavra in list_nova_linha:
                frase += palavra + " "
            
            list_novo.append(frase)

        for linha in list_novo:
            texto_novo += linha + "\n"
    
    texto_novo += "server-id = " + str(gerenciador.id_maquina) + "\n"
    texto_novo += "log_bin = /var/log/mysql/mysql-bin.log" + "\n"
    texto_novo += "log_bin_index =/var/log/mysql/mysql-bin.log.index" + "\n"
    texto_novo += "relay_log = /var/log/mysql/mysql-relay-bin" + "\n"
    texto_novo += "relay_log_index = /var/log/mysql/mysql-relay-bin.index" + "\n"

    print(texto_novo)
    # arquivo_teste = open("arquivo-teste.txt", "w")
    # arquivo_teste.write(texto_novo)

    with open("/etc/mysql/mysql.conf.d/mysqld.cnf", "w") as arquivo:
        arquivo.write(texto_novo)

    os.system("sudo service mysql restart ")

    app.run(debug = True, host = "0.0.0.0")

main(gerenciador)
