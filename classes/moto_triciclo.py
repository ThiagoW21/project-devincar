from classes.veiculo import Veiculo


class MotoTriciclo(Veiculo):
    def __init__(self, manufacturing_date, name, board, price, color, number_of_wheels, potency):
        super().__init__(manufacturing_date, name, board, price, color)
        self.__number_of_wheels = number_of_wheels
        self.__potency = potency

    def data_vehicle(self):
        return {
            **super().data_vehicle,
            'Potencia': self.__potency,
            'Rodas': self.__number_of_wheels
        }
