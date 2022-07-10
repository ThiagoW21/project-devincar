from classes.veiculo import Veiculo
from tinydb import TinyDB
from datetime import date

today = date.today().strftime("%d/%m/%Y")

# Reproduzindo código da documentação do tinyDB
# https://tinydb.readthedocs.io/en/latest/getting-started.html

db = TinyDB('db.json')


class Carro(Veiculo):
    def __init__(self, manufacturing_date, name, board, price, color, potency, fuel_type, total_doors):
        super().__init__(manufacturing_date, name, board, price, color)
        self.__fuel_type = fuel_type
        self.__potency = potency
        self.__total_doors = total_doors

    @property
    def data_vehicle(self):
        return {
            **super().data_vehicle,
            'portas': self.__total_doors,
            'rodas': self.__fuel_type,
            'potencia': self.__potency,
            'combustivel': self.__fuel_type,
        }

    def sell_vehicle(self):
        self.sold = True

        db.insert({
            **super().data_vehicle,
            'portas': self.__total_doors,
            'rodas': self.__fuel_type,
            'potencia': self.__potency,
            'combustivel': self.__fuel_type,
            'data_compra': today
        })