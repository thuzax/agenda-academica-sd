import mysql.connector

class ControllerTarefa:
    instancia = None
    # Singleton
    class __ControllerTarefa:
        # TODO: passar a tarefa por parametro
        def adicionarTarefa(self):
            try:
                conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")
                cursor = conexao.cursor()

                # id_usuario = self.__adicionaDono(conexao, cursor)

                insere_tarefa = ("INSERT INTO Tarefa (data, horario, titulo, descricao, dono_id) "
                                "VALUES (" + "'2018-12-25'" + ", " + "'12:12:00'" + ", " + "'thuza tirou aparelho'" + ", " + "'thuza'" + ", " + "16" + ") "
                                ";")
                print(insere_tarefa)

                cursor.execute(insere_tarefa)
                conexao.commit()
                cursor.close()
                conexao.close()
            except mysql.connector.Error as erro:
                print(erro)
            else:
                conexao.close()
            print("------------------------------------------")

    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__ControllerTarefa()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)


    
