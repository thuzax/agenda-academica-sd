
import mysql.connector

class Controller:
    # TODO: passar o grupo por parametro


    def __adicionaDono(self, conexao, cursor):
        insere_dono = ("INSERT INTO Dono "
                           "VALUES () "
                           ";")

        cursor.execute(insere_dono)
        conexao.commit()
        return cursor.lastrowid

    def adicionarGrupo(self):
        try:
            conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()
            
            id_grupo = self.__adicionaDono(conexao, cursor)



            # print(id_grupo)
            insere_grupo = ("INSERT INTO Grupo (dono_id, nome) "
                            "VALUES (" + str(id_grupo) + ", " + "'teste'" + ") "
                            ";")
            print(insere_grupo)
            
            cursor.execute(insere_grupo)
            conexao.commit()
            cursor.close()
            conexao.close()
        
        except mysql.connector.Error as erro:
            print(erro)

        else:
            conexao.close()
        print("------------------------------------------")

    # TODO: passar o usuario por parametro
    def adicionarUsuario(self):
        try:
            conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()

            id_usuario = self.__adicionaDono(conexao, cursor)

            insere_usuario = ("INSERT INTO Usuario (dono_id, nome, login, senha) "
                            "VALUES (" + str(id_usuario) + ", " + "'thuza'" + ", " + "'thuza'" + ", " + "'thuza'" + ") "
                            ";")
            print(insere_usuario)

            cursor.execute(insere_usuario)
            conexao.commit()
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            print(erro)
        else:
            conexao.close()
        print("------------------------------------------")

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
