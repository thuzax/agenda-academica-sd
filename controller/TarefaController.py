from model.Tarefa import Tarefa

from dao.TarefaDAO import TarefaDAO
from dao.GrupoHasUsuarioDAO import GrupoHasUsuarioDAO

import mysql.connector

class TarefaController:
    instancia = None
    # Singleton
    class __TarefaController:
        def adicionarTarefa(self, data, horario, titulo, descricao, dono_id):
            tarefa = Tarefa(data, horario, titulo, descricao, dono_id)

            TarefaDAO().adicionarTarefa(tarefa)
            
        def buscarTarefasDono(self, dono_id):
            tarefas = TarefaDAO().buscarTarefasDono(dono_id)
            
            return tarefas
        
        def buscarTarefasData(self, dono_id, data):
            grupos_participante = GrupoHasUsuarioDAO().buscarGruposParticipante(dono_id)
            
            tarefas_dono = TarefaDAO().buscarTarefasData(dono_id, data)
            
            tarefas_grupo = []
            if(len(grupos_participante) > 0):
                for grupo in grupos_participante:
                    tarefas_grupo += TarefaDAO().buscarTarefasData(grupo["grupo_id"], data)
            
            tarefas = tarefas_dono + tarefas_grupo

            return tarefas

        def buscarTodasTarefasDono(self, dono_id):
            grupos_participante = GrupoHasUsuarioDAO().buscarGruposParticipante(dono_id)
            
            tarefas_dono = TarefaDAO().buscarTarefasDono(dono_id)
            for grupo_participante in grupos_participante:
                tarefas_grupo = TarefaDAO().buscarTarefasDono(grupo_participante["grupo_id"])
                tarefas_dono += tarefas_grupo

            return tarefas_dono
    


    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__TarefaController()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)


    
