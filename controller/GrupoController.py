
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

            list_grupos = []
            for grupo in grupos:
                list_grupos.append({})
                list_grupos[-1]["nome"] = grupo[0]
                list_grupos[-1]["dono_id"] = grupo[1]
                list_grupos[-1]["participa"] = ""
                list_grupos[-1]["eh_administrador"] = ""

            print(usuario_id)
            if(usuario_id != ""):
                for dict_grupo in list_grupos:
                    if(GrupoHasUsuarioController().participaGrupo(usuario_id, dict_grupo["dono_id"])):
                        dict_grupo["participa"] = "true"
                        if(GrupoHasUsuarioController().ehAdministrador(usuario_id, dict_grupo["dono_id"])):
                            dict_grupo["eh_administrador"] = "true"
                        else:
                            dict_grupo["eh_administrador"] = "false"
                            
                    else:
                        dict_grupo["participa"] = "false"
                        

            return list_grupos
            

    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__GrupoController()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)



     
    