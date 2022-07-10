from classes.veiculo import Veiculo
from tinydb import TinyDB
from datetime import date

today = date.today().strftime("%d/%m/%Y")


# Reproduzindo código da documentação do tinyDB
# https://tinydb.readthedocs.io/en/latest/getting-started.html

db = TinyDB('db.json')


class MotoTriciclo(Veiculo):
    def __init__(self, manufacturing_date, name, board, price, color, potency, number_of_wheels, fuel_type):
        super().__init__(manufacturing_date, name, board, price, color)
        self.__number_of_wheels = number_of_wheels
        self.__potency = potency
        self.__fuel_type = fuel_type

    @property
    def data_vehicle(self):
        return {
            **super().data_vehicle,
            'potencia': self.__potency,
            'rodas': self.__number_of_wheels,
            'combustivel': self.__fuel_type,
        }

    def sell_vehicle(self):
        self.sold = True

        db.insert({
            **super().data_vehicle,
            'potencia': self.__potency,
            'rodas': self.__number_of_wheels,
            'combustivel': self.__fuel_type,
            'data_compra': today
        })
