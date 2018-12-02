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
            
            list_tarefas = []
            for item in tarefas:
                list_tarefas.append({})
                list_tarefas[-1]["id"] = item[0]
                list_tarefas[-1]["data"] = item[1]
                list_tarefas[-1]["horario"] = item[2]
                list_tarefas[-1]["titulo"] = item[3]
                list_tarefas[-1]["descricao"] = item[4]
                list_tarefas[-1]["dono_id"] = item[5]
            
            return list_tarefas
        
        def buscarTarefasData(self, dono_id, data):
            grupos_participante = GrupoHasUsuarioDAO().buscarGruposParticipante(dono_id)
            
            tarefas_dono = TarefaDAO().buscarTarefasData(dono_id, data)
            
            tarefas_grupo = []
            if(len(grupos_participante) > 0):
                for grupo in grupos_participante:
                    tarefas_grupo += TarefaDAO().buscarTarefasData(grupo[1], data)
            
            tarefas = tarefas_dono + tarefas_grupo
            list_tarefas = []
            for item in tarefas:
                list_tarefas.append({})
                list_tarefas[-1]["id"] = item[0]
                list_tarefas[-1]["data"] = item[1]
                list_tarefas[-1]["horario"] = item[2]
                list_tarefas[-1]["titulo"] = item[3]
                list_tarefas[-1]["descricao"] = item[4]
                list_tarefas[-1]["dono_id"] = item[5]

            return list_tarefas


        
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__TarefaController()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)


    
