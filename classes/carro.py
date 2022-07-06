from classes.veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, manufacturing_date, name, board, price, color, ):
        super().__init__(manufacturing_date, name, board, price, color)
