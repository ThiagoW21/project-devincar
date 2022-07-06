import uuid
from tinydb import TinyDB


# Reproduzindo código da documentação do tinyDB
# https://tinydb.readthedocs.io/en/latest/getting-started.html

db = TinyDB('db.json')


class Veiculo:
    def __init__(self, manufacturing_date, name, board, price, color, cpf_buyer=0):
        self.__chassi = str(uuid.uuid4())
        self.__manufacturing_date = manufacturing_date
        self.__name = name
        self.__board = board
        self.__price = price
        self.__cpf_buyer = cpf_buyer
        self.__color = color
        self.__data_vehicle = {
            'Nome': name,
            'Placa': board,
            'Price': price,
            'CPF comprador': self.__cpf_buyer,
            'Cor': color,
            'Data de fabricação': manufacturing_date,
            'Chassi': self.__chassi
        }

    @property
    def data_vehicle(self):
        return self.__data_vehicle

    @property
    def color(self):
        return self.__color

    @property
    def price(self):
        return self.__price

    @color.setter
    def color(self, color):
        if color and len(color) > 2:
            self.__color = color

        else:
            raise TypeError('Informe uma cor válida.')

    @price.setter
    def price(self, price):
        if price > 100 and isinstance(price, float):
            self.__price = price

        else:
            raise TypeError('Informe um valor real maior que 100.')

    @data_vehicle.getter
    def list_information(self):
        return self.__data_vehicle

    def sell_vehicle(self):
        db.insert(self.data_vehicle)
