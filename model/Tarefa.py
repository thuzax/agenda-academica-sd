class Tarefa:
    def __init__(self, data, horario, titulo, descricao, dono_id):
        self.id = None
        self.dono_id = dono_id
        self.data = data
        self.horario = horario
        self.titulo = titulo
        self.descricao = descricao
    
    def getId(self):
        return self.id

    def getDonoId(self):
        return self.dono_id
    
    def getData(self):
        return self.data
    
    def getHorario(self):
        return self.horario
    
    def getTitulo(self):
        return self.titulo
    
    def getDescricao(self):
        return self.descricao

    