import mysql.connector

class GrupoDAO:
    instancia = None
    # Singleton
    class __GrupoDAO:
        def adicionarGrupo(self, grupo):
            print("--------------------------------")
            
            conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()

            insere_grupo = ("INSERT INTO Grupo (dono_id, nome) "
                            "VALUES ('" + str(grupo.getId()) + "', '" + str(grupo.getNome()) + "') "
                            ";")

            print(insere_grupo)

            cursor.execute(insere_grupo)
            conexao.commit()

            cursor.close()
            conexao.close()

            print("------------------------------------------")

        def buscarGrupoPorId(self, grupo_id):
            conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()

            busca_grupos = ("SELECT * FROM Grupo g "
                           "WHERE g.dono_id = '" + str(grupo_id) + "'"
                           ";")

            print(busca_grupos)

            cursor.execute(busca_grupos)
            grupos = cursor.fetchall()
            
            conexao.commit()
            cursor.close()
            conexao.close()

            return grupos


        def buscarTodosGrupos(self):
            conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()

            busca_grupos = ("SELECT * FROM Grupo;"
                           ";")

            print(busca_grupos)

            cursor.execute(busca_grupos)
            grupos = cursor.fetchall()
            
            conexao.commit()
            cursor.close()
            conexao.close()

            return grupos

    # Singleton
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__GrupoDAO()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)