import mysql.connector

class UsuarioDAO:
    instancia = None
    # Singleton
    class __UsuarioDAO:
        def adicionarUsuario(self, usuario):
            print("--------------------------------")
            
            conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")
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


    # Singleton
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__UsuarioDAO()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)