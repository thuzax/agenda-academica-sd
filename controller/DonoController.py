
from model.Dono import Dono
from dao.DonoDAO import DonoDAO
import mysql.connector

class DonoController:
    instancia = None
    # Singleton
    class __DonoController:
        def adicionaDono(self):
            dono = Dono()
            DonoDAO().adicionarDono(dono)
            return dono

    # Singleton
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__DonoController()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)


    


    