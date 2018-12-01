from model.Tarefa import Tarefa

from dao.TarefaDAO import TarefaDAO

import mysql.connector

class TarefaController:
    instancia = None
    # Singleton
    class __TarefaController:
        def adicionarTarefa(self, data, horario, titulo, descricao, dono_id):
            tarefa = Tarefa(data, horario, titulo, descricao, dono_id)

            TarefaDAO().adicionarTarefa(tarefa)
            
        def buscaTarefasDono(self, dono_id):
            list_tarefas = TarefaDAO().buscaTarefasDono(dono_id)
            return list_tarefas
            
        
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__TarefaController()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)


    
