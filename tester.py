import requests
import json

route = "http://127.0.0.1:5000/"
route_adicionar = route + "adicionar/"
route_adicionar_usuario = route_adicionar + "usuario"
route_adicionar_grupo = route_adicionar + "grupo"
route_adicionar_tarefa = route_adicionar + "tarefa"
route_entrar_grupo = route + "entrar_grupo"
route_busca = route + "buscar/"
route_busca_tarefas_dono = route_busca + "tarefas_dono"
route_busca_grupos = route_busca + "grupos"


def insereUsuario():
    query_adicionar_usuario = {}
    query_adicionar_usuario["nome"] = input("Digite o nome do usuario: ")
    query_adicionar_usuario["login"] = input("Digite o login do usuario: ")
    query_adicionar_usuario["senha"] = input("Digite a senha do usuario: ")
    print(query_adicionar_usuario)

    result_adicionar_usuario = requests.post(route_adicionar_usuario, json = json.dumps(query_adicionar_usuario))
    body_usuario = result_adicionar_usuario.content
    response_dict_usuario = json.loads(body_usuario.decode("utf-8"))

    print(response_dict_usuario)


def insereGrupo():
    query_adicionar_grupo = {}
    query_adicionar_grupo["nome"] = input("Digite o nome do grupo: ")
    print(query_adicionar_grupo)

    result_adicionar_grupo = requests.post(route_adicionar_grupo, json = json.dumps(query_adicionar_grupo))
    body_grupo = result_adicionar_grupo.content
    response_dict_grupo = json.loads(body_grupo.decode("utf-8"))
    
    print(response_dict_grupo)


def insereTarefa():
    query_adicionar_tarefa = {}
    query_adicionar_tarefa["titulo"] = input("Digite o titulo da tarefa: ")
    query_adicionar_tarefa["data"] = input("Digite a data (yyyy-mm-dd) da tarefa: ")
    query_adicionar_tarefa["horario"] = input("Digite o horario (hh:mm) da tarefa: ")
    query_adicionar_tarefa["horario"] += ":00"
    query_adicionar_tarefa["descricao"] = input("Digite a descricao da tarefa: ")
    query_adicionar_tarefa["dono_id"] = input("Digite o id do dono da tarefa: ")
    print(query_adicionar_tarefa)

    result_adicionar_tarefa = requests.post(route_adicionar_tarefa, json = json.dumps(query_adicionar_tarefa))
    body_tarefa = result_adicionar_tarefa.content
    response_dict_tarefa = json.loads(body_tarefa.decode("utf-8"))
    
    print(response_dict_tarefa)


def entraGrupo():
    query_entrar_grupo = {}
    query_entrar_grupo["usuario_id"] = input("Digite id do usuario: ")
    query_entrar_grupo["grupo_id"] = input("Digite id do grupo: ")
    texto = "Digite 's' se for admistrador (caso contrario, digite qualquer merda): "
    query_entrar_grupo["eh_administrador"] = 1 if input(texto) == 's' else 0
    print(query_entrar_grupo)

    result_entrar_grupo = requests.post(route_entrar_grupo, json = json.dumps(query_entrar_grupo))
    body_entrar_grupo = result_entrar_grupo.content
    response_dict_entrar_grupo = json.loads(body_entrar_grupo.decode("utf-8"))

    print(response_dict_entrar_grupo)

def buscaTarefasPorId():
    query_busca_tarefas_dono = {}
    query_busca_tarefas_dono["dono_id"] = input("Digite o id do dono das tarefas: ")
    print(query_busca_tarefas_dono)

    result_busca_tarefas_dono = requests.get(route_busca_tarefas_dono, json = json.dumps(query_busca_tarefas_dono))
    body_busca_tarefas_dono = result_busca_tarefas_dono.content
    response_dict_busca_tarefas_dono = json.loads(body_busca_tarefas_dono.decode("utf-8"))

    print(response_dict_busca_tarefas_dono)

def buscaGrupos():
    query_busca_grupos = {}
    texto = "Digite o id do grupo (por padrao busca todos os grupo): "
    query_busca_grupos["grupo_id"] = input(texto)
    texto = "Digite o id do usuario que esta buscando (por padrao nao checa se participa ou se e adm): "
    query_busca_grupos["usuario_id"] = input(texto)
    print(query_busca_grupos)

    result_busca_grupos = requests.get(route_busca_grupos, json = json.dumps(query_busca_grupos))
    body_busca_grupos = result_busca_grupos.content
    response_dict_busca_grupos = json.loads(body_busca_grupos.decode("utf-8"))

    print(response_dict_busca_grupos)

def login():
    query_login = {}
    texto = "Digite o login: "
    query_login["login"] = input(texto)
    texto = "Digite a senha: "
    query_login["senha"] = input(texto)
    print(query_login)

    result_login = requests.get(route_login, json = json.dumps(query_login))
    body_login = result_login.content
    response_dict_login = json.loads(body_login.decode("utf-8"))

    print(response_dict_login)

def mostraOpcoes():
    texto = ""
    texto += "----------------------------------------" + "\n"
    texto += "Escolha uma das opcoes a seguir:" + "\n"
    texto += "1 - Insere usuario" + "\n"
    texto += "2 - Insere grupo" + "\n"
    texto += "3 - Insere tarefa" + "\n"
    texto += "4 - Insere entrar grupo" + "\n"
    texto += "5 - Busca tarefas usando ID do dono" + "\n"
    texto += "6 - Busca grupos (inclui informacao de participacao e se e adm)" + "\n"
    texto += "7 - Fazer Login" + "\n"
    texto += "0 - Sair" + "\n"
    texto += "----------------------------------------" + "\n"
    texto += "Opcao: "
    return input(texto)

    


def fazOpcao(x):
    if(x == "1"):
        insereUsuario()
        return
    if(x == "2"):
        insereGrupo()
        return
    if(x == "3"):
        insereTarefa()
        return
    if(x == "4"):
        entraGrupo()
        return
    if(x == "5"):
        buscaTarefasPorId()
        return
    if(x == "6"):
        buscaGrupos()
        return
    if(x == "7"):
        login()
        return
    print("ERRO")
    return


def main():
    x = mostraOpcoes()
    while(x != "0"):
        fazOpcao(x)
        x = mostraOpcoes()


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

'''
asdasd
adsdas
kvspskdop
2001-10-10
12:12
plaplapla
1

'''