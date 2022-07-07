from classes.moto_triciclo import MotoTriciclo
from classes.carro import Carro

if __name__ == '__main__':
    moto_ciclo = MotoTriciclo('07-08-2000', 'Fiat', 432423, 432, 300, 3, 300)
    carro = Carro('07-08-2000', 'Fiat', 432423, 432, 'black', 3, 300)
    moto_ciclo.color = 'azul'
    moto_ciclo.price = 143
    print(carro.data_vehicle)
