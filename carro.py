from veiculo import Veiculo 
class Carro(Veiculo):
    def __init__(self, placa, modelo, ano, motor, portas):
        super().__init__(placa, modelo, ano, motor)
        self.portas = portas
    def calcular_diaria(self):
        return 120