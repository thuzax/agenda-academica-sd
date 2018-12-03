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
            conexao = mysql.connector.connect(user = "root", password = "32658254", host = "127.0.0.1", database = "agenda-academica")
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

        def sair(self, usuario_id, grupo_id):
            conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "192.168.43.134", database = "agenda-academica")
            cursor = conexao.cursor()

            delete_relacao = ("DELETE FROM Grupo_has_Usuario "
                             "WHERE usuario_id = '" + str(usuario_id) + "' AND grupo_id = '" + str(grupo_id) + "'"
                             ";")

            print(delete_relacao)

            cursor.execute(delete_relacao)
            # relacoes = cursor.fetchall()

            conexao.commit()
            cursor.close()
            conexao.close()

        def buscarGruposParticipante(self, usuario_id):
            conexao = mysql.connector.connect(user = "root", password = "32658254", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()

            busca_grupos = ("SELECT * FROM Grupo_has_Usuario ghu "
                             "WHERE ghu.usuario_id = '" + str(usuario_id) + "'"
                             ";")

            print(busca_grupos)

            cursor.execute(busca_grupos)
            grupos = cursor.fetchall()

            grupos = self.__converteParaLista(grupos)

            conexao.commit()
            cursor.close()
            conexao.close()

            return grupos

        def __converteParaLista(self, grupos_participante):
            list_grupos_participante = []
            for grupo_participante in grupos_participante:
                list_grupos_participante.append({})
                list_grupos_participante[-1]["eh_administrador"] = grupo_participante[0]
                list_grupos_participante[-1]["grupo_id"] = grupo_participante[1]
                list_grupos_participante[-1]["usuario_id"] = grupo_participante[2]
            return list_grupos_participante
    # Singleton
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__GrupoHasUsuarioDAO()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)