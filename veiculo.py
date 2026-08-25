from motor import Motor

class Veiculo:
    def __init__(self, placa, modelo, ano, motor):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.motor = Motor

    def calcular_diaria(self):
        return 100
    
    def mostrar_info(self):
        return f"{self.placa} |{self.modelo} | {self.ano}"
    