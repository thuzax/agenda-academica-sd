import socket
import requests
import sys
import json
import os
from flask import Flask, redirect, url_for, request, Response, jsonify
import mysql.connector


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


def redirecionaRequisicao(route, dados):
    gerenciador.setMasterRoute()
    result = requests.post(route, json = dados)
    
    body = result.content
    print(body)
    response_dict = json.loads(body.decode("utf-8"))
    print(response_dict)

    
    return response_dict

@app.route('/adicionar/usuario',methods = ['POST'])
def adicionarUsuario():
    dados = getJsonFromRequest(request)
    if(gerenciador.master_ip != gerenciador.my_ip):
        response_dict = redirecionaRequisicao(gerenciador.route_adicionar_usuario, dados)
        response = Response(json.dumps({"usuario_id" : response_dict["usuario_id"]}), status=200, mimetype='application/json')
        return response
    
    usuario_id = UsuarioController().adicionarUsuario(dados["nome"], dados["login"], dados["senha"])
    response = Response(json.dumps({"usuario_id" : usuario_id}), status=200, mimetype='application/json')
    return response
        
    
@app.route('/adicionar/grupo',methods = ['POST'])
def adicionarGrupo():
    dados = getJsonFromRequest(request)
    if(gerenciador.master_ip != gerenciador.my_ip):
        response_dict = redirecionaRequisicao(gerenciador.route_adicionar_grupo, dados)
        response = Response(json.dumps(dados), status=200, mimetype='application/json')
        return response
    GrupoController().adicionarGrupo(dados["nome"])
    response = Response(json.dumps(dados), status=200, mimetype='application/json')
    return response

@app.route('/adicionar/tarefa',methods = ['POST'])
def adicionarTarefa():
    dados = getJsonFromRequest(request)
    if(gerenciador.master_ip != gerenciador.my_ip):
        response_dict = redirecionaRequisicao(gerenciador.route_adicionar_tarefa, dados)
        response = Response(json.dumps(dados), status=200, mimetype='application/json')
        return response
    t_id = TarefaController().adicionarTarefa(dados["data"], dados["horario"], dados["titulo"], dados["descricao"], dados["dono_id"])
    dados["id"] = t_id
    response = Response(json.dumps(dados), status=200, mimetype='application/json')
    return response

@app.route('/entrar_grupo', methods = ["POST"])
def entrarGrupo():
    dados = getJsonFromRequest(request)
    if(gerenciador.master_ip != gerenciador.my_ip):
        response_dict = redirecionaRequisicao(gerenciador.route_entrar_grupo, dados)
        response = Response(json.dumps(dados), status=200, mimetype='application/json')
        return response
    GrupoHasUsuarioController().entrarGrupo(dados["usuario_id"], dados["grupo_id"], dados["eh_administrador"])
    response =  Response(json.dumps(dados), status=200, mimetype='application/json')
    return response

@app.route('/buscar/tarefas/todos/dono', methods = ["GET"])
def buscarTodasTarefasDono():
    dados = getParamsFromRequest(request)
    tarefas = TarefaController().buscarTodasTarefasDono(dados["dono_id"])
    response =  Response(json.dumps(tarefas), status=200, mimetype='application/json')
    return response


@app.route('/buscar/tarefas/dono', methods = ["GET"])
def buscarTarefaDono():
    dados = getParamsFromRequest(request)
    tarefas = TarefaController().buscarTarefasDono(dados["dono_id"])
    response =  Response(json.dumps(tarefas), status=200, mimetype='application/json')
    return response

@app.route('/buscar/tarefas/data', methods = ["GET"])
def buscarTarefasData():
    dados = getParamsFromRequest(request)
    print(dados)
    tarefas = TarefaController().buscarTarefasData(dados["dono_id"])
    print(tarefas)
    response =  Response(json.dumps(tarefas), status=200, mimetype='application/json')
    return response


@app.route('/buscar/grupos/id_ou_user', methods = ["GET"])
def buscarGrupos():
    dados = getParamsFromRequest(request)
    grupos = GrupoController().buscarGrupos(dados["grupo_id"], dados["usuario_id"])
    response =  Response(json.dumps(grupos), status=200, mimetype='application/json')
    return response

@app.route('/login', methods = ["POST"])
def login():
    dados = getJsonFromRequest(request)
    usuario_id = UsuarioController().login(dados["login"], dados["senha"])
    print("usuario_id")
    response = Response(json.dumps({"usuario_id" : usuario_id}), status=200, mimetype='application/json')
    return response


@app.route('/sair_grupo', methods = ["POST"])
def sairGrupo():
    dados = getJsonFromRequest(request)
    if(gerenciador.master_ip != gerenciador.my_ip):
        response_dict = redirecionaRequisicao(gerenciador.route_sair_grupo, dados)
        response = Response(json.dumps({"mensagem" : "ok"}), status=200, mimetype='application/json')
        return response
    GrupoHasUsuarioController().sair(dados["usuario_id"], dados["grupo_id"])
    response = Response(json.dumps({"mensagem" : "ok"}), status=200, mimetype='application/json')
    return response


@app.route('/buscar/grupos/participante', methods = ["GET"])
def buscarGruposParticipante():
    dados = getParamsFromRequest(request)
    grupos_participante = GrupoHasUsuarioController().buscarGruposParticipante(dados["usuario_id"])
    response = Response(json.dumps(grupos_participante), status=200, mimetype='application/json')
    return response



@app.route('/ping_master', methods = ["GET"])
def pingMaster():
    response =  Response(json.dumps(gerenciador.master_ip), status=200, mimetype='application/json')
    return response


def getParamsFromRequest(request):
    dados = request.args.to_dict()
    return dados

def getJsonFromRequest(request):
    dados = request.get_json()
    return dados

def getMyIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ip = s.connect(("8.8.8.8", 80))
    except:
        ip = "192.168.43.82"
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


# def createMySQLConnection(gerenciador):
    # print("------------------------------")
    # conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1")
    # cursor = conexao.cursor()
    # cursor.execute("set global server_id = " + str(gerenciador.id_maquina + ";"))
    # cursor.execute("set global server_id = " + str(gerenciador.id_maquina + ";"))
    # print(cursor.fetchall())
    # conexao.commit()
    # cursor.execute("select @@server_id")
    # print(cursor.fetchall())
    # cursor.execute("drop schema if exists `agenda-academica`;")
    # conexao.commit()
    # cursor.execute("create schema if not exists `agenda-academica`;")
    # conexao.commit()
    # cursor.close()
    # conexao.close()
    # print("------------------------------")

    

    # comando = "mysqldump -h 192.168.1.3 -u thuza -p agenda-academica | mysql -h 127.0.0.1 -u thuza -p agenda-academica"
    # os.system(comando)
    

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

    # texto_novo = ""
    # with open("banco-de-dados/mysqld.cnf", "r") as arquivo:
    #     entrada = arquivo.read().strip().splitlines()
    #     list_novo = []
    #     for linha in entrada:
    #         list_linha = linha.strip().split()
    #         list_nova_linha = []
            
    #         i = 0
    #         while(i < len(list_linha)):
    #             if(list_linha[i] == "bind-address"):
    #                 if(list_linha[i + 1] == "="):
    #                     if(list_linha[i + 2] == "127.0.0.1"):
    #                         list_nova_linha.append(list_linha[i])
    #                         list_nova_linha.append(list_linha[i + 1])
    #                         list_nova_linha.append("0.0.0.0")
    #                         i += 3
    #                         continue
    #             list_nova_linha.append(list_linha[i])
    #             i += 1
            
    #         frase = ""
    #         for palavra in list_nova_linha:
    #             frase += palavra + " "
            
    #         list_novo.append(frase)

    #     for linha in list_novo:
    #         texto_novo += linha + "\n"
    
    # texto_novo += "log_bin = /var/log/mysql/mysql-bin.log" + "\n"
    # texto_novo += "log_bin_index =/var/log/mysql/mysql-bin.log.index" + "\n"
    # texto_novo += "relay_log = /var/log/mysql/mysql-relay-bin" + "\n"
    # texto_novo += "relay_log_index = /var/log/mysql/mysql-relay-bin.index" + "\n"


    # with open("/etc/mysql/mysql.conf.d/mysqld.cnf", "w") as arquivo:
    #     arquivo.write(texto_novo)

    # os.system("sudo service mysql restart")

    # createMySQLConnection(gerenciador)

    app.run(debug = True, host = "0.0.0.0")


main(gerenciador)
