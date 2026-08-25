class Aluguel:
    def __init__(self, cliente, veiculo, dias): 
        self.cliente = cliente 
        self.veiculo = veiculo 
        self.dias = dias 
    def calcular_valor(self): 
        return self.veiculo.calcular_diaria() * self.dias 
    def mostrar_info(self): 
        return (
            f"Cliente: {self.cliente.nome}\n"
            f"Veículo: {self.veiculo.modelo}\n"
            f"Dias: {self.dias}\n"
            f"Valor: R${self.calcular_valor():.2f}"
        )