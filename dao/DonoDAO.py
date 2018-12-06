import mysql.connector

class DonoDAO:
    instancia = None
    # Singleton
    class __DonoDAO:
        def adicionarDono(self, dono):
            print("--------------------------------")
            conexao = mysql.connector.connect(user = "root", password = "32658254", host = "127.0.0.1", database = "agenda-academica")
            cursor = conexao.cursor()

            insere_dono = ("INSERT INTO Dono "
                                "VALUES () "
                                ";")
            print(insere_dono)
            
            cursor.execute(insere_dono)
            conexao.commit()
            dono.setId(cursor.lastrowid)

            cursor.close()
            conexao.close()
            print("--------------------------------")

    # Singleton
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__DonoDAO()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)