import mysql.connector

class GrupoHasUsuarioDAO:
    instancia = None
    # Singleton
    class __GrupoHasUsuarioDAO:
        def entrarGrupo(self, grupo_has_usuario):
            print("--------------------------------")
            
            conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()

            insere_entra_grupo = ("INSERT INTO Grupo_has_Usuario (grupo_id, usuario_id, eh_admin) "
                                  "VALUES ('" + str(grupo_has_usuario.getGrupoId()) + "', '" + str(grupo_has_usuario.getUsuarioId()) + "', '" + str(grupo_has_usuario.getEhAdministrador()) + "') "
                                  ";")

            print(insere_entra_grupo)

            cursor.execute(insere_entra_grupo)
            conexao.commit()

            cursor.close()
            conexao.close()

            print("------------------------------------------")

        def buscaRelacao(self, usuario_id, grupo_id):
            conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()

            busca_relacao = ("SELECT * FROM Grupo_has_Usuario ghu "
                             "WHERE ghu.usuario_id = '" + str(usuario_id) + "' AND ghu.grupo_id = '" + str(grupo_id) + "'"
                             ";")

            print(busca_relacao)

            cursor.execute(busca_relacao)
            relacoes = cursor.fetchall()

            conexao.commit()
            cursor.close()
            conexao.close()

            return relacoes

    # Singleton
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__GrupoHasUsuarioDAO()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)