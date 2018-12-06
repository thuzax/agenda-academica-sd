import mysql.connector

class GrupoDAO:
    instancia = None
    # Singleton
    class __GrupoDAO:
        def adicionarGrupo(self, grupo):
            print("--------------------------------")
            
            conexao = mysql.connector.connect(user = "root", password = "32658254", host = "127.0.0.1", database = "agenda-academica")
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
            conexao = mysql.connector.connect(user = "root", password = "32658254", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()

            busca_grupos = ("SELECT * FROM Grupo g "
                           "WHERE g.dono_id = '" + str(grupo_id) + "'"
                           ";")

            print(busca_grupos)

            cursor.execute(busca_grupos)
            grupos = cursor.fetchall()
            grupos = self.__converteParaLista(grupos)

            conexao.commit()
            cursor.close()
            conexao.close()

            return grupos


        def buscarTodosGrupos(self):
            conexao = mysql.connector.connect(user = "root", password = "32658254", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()

            busca_grupos = ("SELECT * FROM Grupo;"
                           ";")

            print(busca_grupos)

            cursor.execute(busca_grupos)
            grupos = cursor.fetchall()
            grupos = self.__converteParaLista(grupos)

            conexao.commit()
            cursor.close()
            conexao.close()

            print("++++++++++++++++++++++++++")
            print(grupos)
            return grupos

        
        def __converteParaLista(self, grupos):
            list_grupos = []
            for grupo in grupos:
                list_grupos.append({})
                list_grupos[-1]["nome"] = grupo[0]
                list_grupos[-1]["dono_id"] = grupo[1]
            return list_grupos

    # Singleton
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__GrupoDAO()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)