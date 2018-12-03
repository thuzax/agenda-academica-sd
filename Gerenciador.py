class Gerenciador:
    def __init__(self):
        self.ips = None
        self.my_ip = ""
        self.master_ip = None
        self.id_maquina = None
        
        self.route = "http://127.0.0.1:5000/"

        self.route_adicionar = self.route + "adicionar/"
        self.route_adicionar_usuario = self.route_adicionar + "usuario"
        self.route_adicionar_grupo = self.route_adicionar + "grupo"
        self.route_adicionar_tarefa = self.route_adicionar + "tarefa"

        self.route_entrar_grupo = self.route + "entrar_grupo"
        self.route_sair_grupo = self.route + "sair_grupo"


        self.route_buscar = self.route + "buscar/"
        self.route_buscar_tarefas = self.route_buscar + "tarefas"
        self.route_buscar_tarefas_dono = self.route_buscar_tarefas + "/dono"
        self.route_buscar_tarefas_data = self.route_buscar_tarefas + "/data"

        self.route_buscar_grupos = self.route_buscar + "grupos/"
        self.route_buscar_grupos_id_ou_user = self.route_buscar_grupos + "id_ou_user"
        self.route_buscar_grupos_participante = self.route_buscar_grupos + "participante"

        self.route_login = self.route + "login"

    def setMasterRoute(self):
        self.route = "http://" + self.master_ip + ":5000/"

        self.route_adicionar = self.route + "adicionar/"
        self.route_adicionar_usuario = self.route_adicionar + "usuario"
        self.route_adicionar_grupo = self.route_adicionar + "grupo"
        self.route_adicionar_tarefa = self.route_adicionar + "tarefa"

        self.route_entrar_grupo = self.route + "entrar_grupo"
        self.route_sair_grupo = self.route + "sair_grupo"


        self.route_buscar = self.route + "buscar/"
        self.route_buscar_tarefas = self.route_buscar + "tarefas"
        self.route_buscar_tarefas_dono = self.route_buscar_tarefas + "/dono"
        self.route_buscar_tarefas_data = self.route_buscar_tarefas + "/data"

        self.route_buscar_grupos = self.route_buscar + "grupos/"
        self.route_buscar_grupos_id_ou_user = self.route_buscar_grupos + "id_ou_user"
        self.route_buscar_grupos_participante = self.route_buscar_grupos + "participante"

        self.route_login = self.route + "login"
