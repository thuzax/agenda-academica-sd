import mysql.connector

class TarefaDAO:
    instancia = None
    # Singleton
    class __TarefaDAO:
        def adicionarTarefa(self, tarefa):
            print("--------------------------------")

            conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()

            insere_tarefa = ("INSERT INTO Tarefa (data, horario, titulo, descricao, dono_id) "
                            "VALUES ('" + str(tarefa.getData()) + "', '" + str(tarefa.getHorario()) + "', '" + str(tarefa.getTitulo()) + "', '" + str(tarefa.getDescricao()) + "', '" + str(tarefa.getDonoId()) + "') "
                            ";")
            print(insere_tarefa)

            cursor.execute(insere_tarefa)
            conexao.commit()
            cursor.close()
            conexao.close()

            print("--------------------------------")

        def buscaTarefasDono(self, dono_id):
            conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")


            cursor = conexao.cursor()

            busca_tarefas = ("SELECT id, DATE_FORMAT(data, '%Y-%m-%d') AS data, DATE_FORMAT(horario, '%H:%i:%s') AS horario, "
                             "titulo, descricao, dono_id "
                             "FROM Tarefa t "
                             "WHERE t.dono_id = '" + str(dono_id) + "'"
                             ";")
            print(busca_tarefas)

            cursor.execute(busca_tarefas)
            tarefas = cursor.fetchall()
            
            conexao.commit()
            cursor.close()
            conexao.close()
            
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

    # Singleton
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__TarefaDAO()

    

    def __getattr__(self, name):
        return getattr(self.instancia, name)