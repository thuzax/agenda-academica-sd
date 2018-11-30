class Usuario:
    
    def __init__(self, dono_id, nome, login, senha):
        self.dono_id = dono_id
        self.nome = nome
        self.login = login
        self.senha = senha
    
    def getId(self):
        return self.dono_id

    def getNome(self):
        return self.nome
    
    def getLogin(self):
        return self.login
    
    def getSenha(self):
        return self.senha