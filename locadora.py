class Locadora:
    def __init__(self, nome):
        self.nome = nome 
        self.veiculos = []
        self.clientes = []
        self.alugueis = []
    def adicionar_veiculos(self, veiculo):
        self.veiculos.append(veiculo)
    def adicionar_clientes(self, cliente):
        self.clientes.append(cliente)   
    def adicionar_alugueis(self, aluguel):
        self.alugueis.append(aluguel)
    def listar_veiculos(self):
        for veiculo in self.veiculos:
            print(veiculo.mostrar_info())

        