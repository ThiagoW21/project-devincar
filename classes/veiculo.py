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

    @property
    def data_vehicle(self):
        return {
            'Nome': self.__name,
            'Placa': self.__board,
            'Price': self.__price,
            'CPF_comprador': self.__cpf_buyer,
            'Cor': self.__color,
            'Data de fabricação': self.__manufacturing_date,
            'Chassi': self.__chassi
        }

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
        if price > 100:
            self.__price = price

        else:
            raise TypeError('Informe um valor real maior que 100.')

    def sell_vehicle(self):
        db.insert({
            'nome': self.__name,
            'placa': self.__board,
            'price': self.__price,
            'cpf_comprador': self.__cpf_buyer,
            'cor': self.__color,
            'data_de_fabricacao': self.__manufacturing_date,
            'chassi': self.__chassi
        })

    @property
    def cpf_comprador(self):
        return self.__cpf_buyer

    @cpf_comprador.setter
    def cpf_comprador(self, cpf):
        if len(cpf) == 11:
            self.__cpf_buyer = cpf
        else:
            raise TypeError('CPF inválido.')
