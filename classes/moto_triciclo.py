from classes.veiculo import Veiculo


class MotoTriciclo(Veiculo):
    def __init__(self, manufacturing_date, name, board, price, color, number_of_wheels, potency, cpf_buyer=0):
        super().__init__(manufacturing_date, name, board, price, color, cpf_buyer)
        self.__number_of_wheels = number_of_wheels
        self.__potency = potency
