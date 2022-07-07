from classes.veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, manufacturing_date, name, board, price, color, is_flex, potency):
        super().__init__(manufacturing_date, name, board, price, color)
        self.__fuel_type = 'flex' if is_flex else 'gasolina'
        self.__potency = potency

    @property
    def data_vehicle(self):
        return {
            **super().data_vehicle,
            'Rodas': self.__fuel_type,
            'Potencia': self.__potency
        }