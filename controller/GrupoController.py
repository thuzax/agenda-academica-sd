
from model.Grupo import Grupo
from dao.GrupoDAO import GrupoDAO

from controller.DonoController import DonoController

import mysql.connector


class GrupoController:
    instancia = None
    # Singleton
    class __GrupoController:
        def adicionarGrupo(self, nome):
            dono_grupo = DonoController().adicionaDono()

            grupo = Grupo(dono_grupo.getId(), nome)
            GrupoDAO().adicionarGrupo(grupo)
            

    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__GrupoController()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)



     
    