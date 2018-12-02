from model.GrupoHasUsuario import GrupoHasUsuario
from dao.GrupoHasUsuarioDAO import GrupoHasUsuarioDAO
from dao.GrupoDAO import GrupoDAO


class GrupoHasUsuarioController:
    instancia = None
    # Singleton
    class __GrupoHasUsuarioController:
        def entrarGrupo(self, usuario_id, grupo_id, eh_administrador):

                grupo_has_usuario = GrupoHasUsuario(usuario_id, grupo_id, eh_administrador)
                GrupoHasUsuarioDAO().entrarGrupo(grupo_has_usuario)


        def participaGrupo(self, usuario_id, grupo_id):
            print(usuario_id, grupo_id)
            relacoes = GrupoHasUsuarioDAO().buscaRelacao(usuario_id, grupo_id)
            print(relacoes)
            if(len(relacoes) > 0):
                return True
            return False

        def ehAdministrador(self, usuario_id, grupo_id):
            print(usuario_id, grupo_id)
            relacoes = GrupoHasUsuarioDAO().buscaRelacao(usuario_id, grupo_id)
            print(relacoes)
            if(len(relacoes) > 0):
                relacao = relacoes[0]
                return (True if relacao[0] == 1 else False)
            return False


        def sair(self, usuario_id, grupo_id):
            GrupoHasUsuarioDAO().sair(usuario_id, grupo_id)

        def buscarGruposParticipante(self, usuario_id):
            grupos_participante = GrupoHasUsuarioDAO().buscarGruposParticipante(usuario_id)
            
            list_grupos_participante = []
            for grupo_participante in grupos_participante:
                list_grupos_participante.append({})
                list_grupos_participante[-1]["eh_administrador"] = grupo_participante[0]
                list_grupos_participante[-1]["grupo_id"] = grupo_participante[1]
                list_grupos_participante[-1]["usuario_id"] = grupo_participante[2]
                grupo = GrupoDAO().buscarGrupoPorId(list_grupos_participante[-1]["grupo_id"])
                list_grupos_participante[-1]["nome"] = grupo[0][0]
            
            return list_grupos_participante



    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__GrupoHasUsuarioController()
    

    def __getattr__(self, name):
        return getattr(self.instancia, name)