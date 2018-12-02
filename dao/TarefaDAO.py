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

        def buscarTarefasDono(self, dono_id):
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
            
            return tarefas

        def buscarTarefasData(self, dono_id, data):
            conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")


            cursor = conexao.cursor()

            busca_tarefas = ("SELECT id, DATE_FORMAT(data, '%Y-%m-%d') AS data, DATE_FORMAT(horario, '%H:%i:%s') AS horario, "
                             "titulo, descricao, dono_id "
                             "FROM Tarefa t "
                             "WHERE t.dono_id = '" + str(dono_id) + "' AND data = '" + str(data) + "'"
                             ";")
            print(busca_tarefas)

            cursor.execute(busca_tarefas)
            tarefas = cursor.fetchall()
            
            conexao.commit()
            cursor.close()
            conexao.close()
            
            return tarefas

    # Singleton
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__TarefaDAO()

    

    def __getattr__(self, name):
        return getattr(self.instancia, name)