import requests
import json

def main():
    
    query_adicionar_usuario = {}
    query_adicionar_usuario["nome"] = input()# ("Digite o nome do usuario:")
    query_adicionar_usuario["login"] = input()# ("Digite o login do usuario:")
    query_adicionar_usuario["senha"] = input()# ("Digite a senha do usuario:")

    query_adicionar_grupo = {}
    query_adicionar_grupo["nome"] = input()# ("Digite o nome do grupo:")

    query_adicionar_tarefa = {}
    query_adicionar_tarefa["titulo"] = input()# ("Digite o titulo da tarefa:")
    query_adicionar_tarefa["data"] = input()# ("Digite a data (yyyy-mm-dd) da tarefa:")
    query_adicionar_tarefa["horario"] = input()# ("Digite o horario (hh:mm) da tarefa:")
    query_adicionar_tarefa["horario"] += ":00"
    query_adicionar_tarefa["descricao"] = input()# ("Digite a descricao da tarefa:")
    query_adicionar_tarefa["dono_id"] = input()# ("Digite o id do dono da tarefa:")

    query_entrar_grupo = {}
    query_entrar_grupo["usuario_id"] = input()
    query_entrar_grupo["grupo_id"] = input()
    query_entrar_grupo["eh_administrador"] = 1 if input() == 's' else 0

    route = "http://127.0.0.1:5000/"
    route_adicionar = route + "adicionar/"
    route_adicionar_usuario = route_adicionar + "usuario"
    route_adicionar_grupo = route_adicionar + "grupo"
    route_adicionar_tarefa = route_adicionar + "tarefa"
    route_entrar_grupo = route + "entrar_grupo"
    
    result_adicionar_usuario = requests.post(route_adicionar_usuario, data = query_adicionar_usuario)
    result_adicionar_grupo = requests.post(route_adicionar_grupo, data = query_adicionar_grupo)
    result_adicionar_tarefa = requests.post(route_adicionar_tarefa, data = query_adicionar_tarefa)
    result_entrar_grupo = requests.post(route_entrar_grupo, data = query_entrar_grupo)
    
    # routeBusca = route + "busca"

    # request = requests.get(routeBusca, data = query)
    body_usuario = result_adicionar_usuario.content
    body_grupo = result_adicionar_grupo.content
    body_tarefa = result_adicionar_tarefa.content
    body_entrar_grupo = result_entrar_grupo.content
    
    response_dict_usuario = body_usuario.decode("utf-8")
    response_dict_grupo = body_grupo.decode("utf-8")
    response_dict_tarefa = body_tarefa.decode("utf-8")
    response_dict_entrar_grupo = body_entrar_grupo.decode("utf-8")
    
    print("*************************************")
    print(response_dict_usuario)
    print("-------------------------------------")
    print(response_dict_grupo)
    print("-------------------------------------")
    print(response_dict_tarefa)
    print("-------------------------------------")
    print(response_dict_entrar_grupo)
    print("*************************************")

main()
'''

thuza
--------
tutu
--------
123
ola
nada
2001-10-10
12:12
nada nada
6

'''
