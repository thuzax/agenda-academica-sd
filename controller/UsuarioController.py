import mysql.connector

from controller.DonoController import DonoController

from model.Usuario import Usuario

from dao.UsuarioDAO import UsuarioDAO

class UsuarioController:
    instancia = None
    # Singleton
    class __UsuarioController:
        def adicionarUsuario(self, nome, login, senha):
                dono_usuario = DonoController().adicionaDono()

                usuario = Usuario(dono_usuario.getId(), nome, login, senha)
                UsuarioDAO().adicionarUsuario(usuario)
                
                return usuario.getId()

        def login(self, login, senha):
            usuario_id = UsuarioDAO().login(login, senha)
            return usuario_id



    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__UsuarioController()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)


    