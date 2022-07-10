import uuid
from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, manufacturing_date, name, board, price, color):
        self.__chassi = str(uuid.uuid4())
        self.__manufacturing_date = manufacturing_date
        self.__name = name
        self.__board = board
        self._price = price
        self._cpf_buyer = 0
        self._color = color
        self._sold = False

    @property
    @abstractmethod
    def data_vehicle(self):
        return {
            'nome': self.__name,
            'placa': self.__board,
            'preco': self._price,
            'cpf_comprador': self._cpf_buyer,
            'cor': self._color,
            'data_fabricacao': self.__manufacturing_date,
            'chassi': self.__chassi,
            'status': 'Vendido' if self._sold else 'Disponível',
        }

    @property
    def color(self):
        return self._color

    @property
    def sold(self):
        return self._sold

    @sold.setter
    def sold(self, value):
        self._sold = value

    @property
    def price(self):
        return self._price

    @color.setter
    def color(self, color):
        self._color = color

    @price.setter
    def price(self, price):
        self._price = price

    @abstractmethod
    def sell_vehicle(self):
        pass

    @property
    def cpf_buyer(self):
        return self._cpf_buyer

    @cpf_buyer.setter
    def cpf_buyer(self, cpf):
        self._cpf_buyer = cpf

    @sold.setter
    def sold(self, value):
        self._sold = value

