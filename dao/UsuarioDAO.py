import mysql.connector

class UsuarioDAO:
    instancia = None
    # Singleton
    class __UsuarioDAO:
        def adicionarUsuario(self, usuario):
            print("--------------------------------")
            
            conexao = mysql.connector.connect(user = "root", password = "32658254", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()


            insere_usuario = ("INSERT INTO Usuario (dono_id, nome, login, senha) "
                                "VALUES ('" + str(usuario.getId()) + "', '" + usuario.getNome() + "', '" + usuario.getLogin() + "', '" + usuario.getSenha() + "') "
                            ";")

            print(insere_usuario)

            cursor.execute(insere_usuario)
            conexao.commit()
            cursor.close()
            conexao.close()

            print("--------------------------------")

        def login(self, login, senha):
            conexao = mysql.connector.connect(user = "root", password = "32658254", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()
            login_usuario = ("SELECT * FROM Usuario u "
                              "WHERE u.login = '" + str(login) + "' AND u.senha = '" + str(senha) + "'"
                              ";")
            print(login_usuario)
            
            cursor.execute(login_usuario)
            usuario_id = cursor.fetchall()
            print(usuario_id)
            
            conexao.commit()
            cursor.close()
            conexao.close()

            return usuario_id

        def buscaLogin(self, login):
            conexao = mysql.connector.connect(user = "root", password = "32658254", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()
            login_usuario = ("SELECT * FROM Usuario u "
                              "WHERE u.login = '" + str(login) + "'"
                              ";")
            print(login_usuario)
            
            cursor.execute(login_usuario)
            usuario_id = cursor.fetchall()
            print(usuario_id)
            
            conexao.commit()
            cursor.close()
            conexao.close()

            return usuario_id


    # Singleton
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__UsuarioDAO()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)