from veiculo import Veiculo 
class Moto(Veiculo):
    def __init__(self, placa, modelo, ano, potencia, cilindradas):
        super().__init__(placa, modelo, ano, potencia)
        self.cilindradas = cilindradas
    def calcular_diaria(self):
        return 80 
    