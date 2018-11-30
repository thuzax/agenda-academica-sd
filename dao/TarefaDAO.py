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

    # Singleton
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__TarefaDAO()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)