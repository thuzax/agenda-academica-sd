
import mysql.connector

class ControllerDono:
    instancia = None
    # Singleton
    class __ControllerDono:
        def adicionaDono(self, conexao, cursor):
            insere_dono = ("INSERT INTO Dono "
                            "VALUES () "
                            ";")

            cursor.execute(insere_dono)
            conexao.commit()
            return cursor.lastrowid

    # Singleton
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__ControllerDono()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)


    


    