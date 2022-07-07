from classes.veiculo import Veiculo


class Caminhonete(Veiculo):
    def __init__(self, manufacturing_date, name, board,
                 price, potency, fuel_type,  total_doors, capacity):

        super().__init__(manufacturing_date, name, board, price, color='Roxo')
        self.__fuel_type = fuel_type
        self.__potency = potency
        self.__total_doors = total_doors
        self.__capacity = capacity

    @property
    def data_vehicle(self):
        return {
            **super().data_vehicle,
            'Portas': self.__total_doors,
            'Rodas': self.__fuel_type,
            'Potencia': self.__potency,
            'Combustivel': self.__fuel_type
        }
