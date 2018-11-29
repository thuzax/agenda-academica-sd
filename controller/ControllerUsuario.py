import mysql.connector

from controller.ControllerDono import ControllerDono


class ControllerUsuario:
    instancia = None
    # Singleton
    class __ControllerUsuario:
        # TODO: passar o usuario por parametro
        def adicionarUsuario(self):
            try:
                conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")
                cursor = conexao.cursor()

                id_usuario = ControllerDono().adicionaDono(conexao, cursor)

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

    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__ControllerUsuario()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)


    