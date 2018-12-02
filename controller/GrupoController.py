
from model.Grupo import Grupo
from dao.GrupoDAO import GrupoDAO

from controller.DonoController import DonoController

from controller.GrupoHasUsuarioController import GrupoHasUsuarioController

import mysql.connector


class GrupoController:
    instancia = None
    # Singleton
    class __GrupoController:
        def adicionarGrupo(self, nome):
            dono_grupo = DonoController().adicionaDono()

            grupo = Grupo(dono_grupo.getId(), nome)
            GrupoDAO().adicionarGrupo(grupo)

        def buscarGrupos(self, grupo_id, usuario_id):
            print(grupo_id)
            if(grupo_id == ""):
                grupos = GrupoDAO().buscarTodosGrupos()
            else:
                grupos = GrupoDAO().buscarGrupoPorId(grupo_id)

            for dict_grupo in grupos:
                dict_grupo["participa"] = ""
                dict_grupo["eh_administrador"] = ""
            print(usuario_id)
            if(usuario_id != ""):
                for dict_grupo in grupos:
                    dict_grupo["participa"] = ""
                    dict_grupo["eh_administrador"] = ""
                    if(GrupoHasUsuarioController().participaGrupo(usuario_id, dict_grupo["dono_id"])):
                        dict_grupo["participa"] = "true"
                        if(GrupoHasUsuarioController().ehAdministrador(usuario_id, dict_grupo["dono_id"])):
                            dict_grupo["eh_administrador"] = "true"
                        else:
                            dict_grupo["eh_administrador"] = "false"
                            
                    else:
                        dict_grupo["participa"] = "false"
                        

            return grupos
            

    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__GrupoController()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)



     
    