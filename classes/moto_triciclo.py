from classes.veiculo import Veiculo


class MotoTriciclo(Veiculo):
    def __init__(self, manufacturing_date, name, board, price, color, number_of_wheels, potency):
        super().__init__(manufacturing_date, name, board, price, color)
        self.number_of_wheels = number_of_wheels
        self.potency = potency

    def compar(self):
        return self.potency
