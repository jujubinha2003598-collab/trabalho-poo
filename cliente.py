class Cliente: 
    def __init__(self, nome, cpf ): 
        self.nome = nome 
        self.cpf = cpf 
    def mostrar_info(self): 
        return f"{self.nome} | {self.cpf}"
    