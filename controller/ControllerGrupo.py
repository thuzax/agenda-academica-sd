import mysql.connector

from controller.ControllerDono import ControllerDono

class ControllerGrupo:
    instancia = None
    # Singleton
    class __ControllerGrupo:
        # TODO: passar o grupo por parametro
        def adicionarGrupo(self):
            try:
                conexao = mysql.connector.connect(user = "thuza", password = "agenda", host = "127.0.0.1", database = "agenda-academica")
                cursor = conexao.cursor()
                
                id_grupo = ControllerDono().adicionaDono(conexao, cursor)



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

    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__ControllerGrupo()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)



     
    