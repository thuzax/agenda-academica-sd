class GrupoHasUsuario:
    def __init__(self, usuario_id, grupo_id, eh_administrador):
        self.grupo_id = grupo_id
        self.usuario_id = usuario_id
        self.eh_administrador = eh_administrador

    def getGrupoId(self):
        return self.grupo_id
    
    def getUsuarioId(self):
        return self.usuario_id

    def getEhAdministrador(self):
        return self.eh_administrador