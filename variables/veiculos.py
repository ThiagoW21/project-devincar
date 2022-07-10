from classes.moto_triciclo import MotoTriciclo
from classes.carro import Carro
from classes.camionete import Camionete


moto_triciclo = {
    'cg_160_start': MotoTriciclo('13/02/2020', 'CG 160 Start', 'NEV-7450', 12000, 'Preto', 100, 2, 'gasolina'),
    'cg_160_fan': MotoTriciclo('22/06/2021', 'CG 160 Fan', 'HTG-3337', 13480, 'Azul', 120, 2, 'gasolina'),
    'pop100_i': MotoTriciclo('11/04/2019', 'POP 100 i', 'HWO-1382', 8330, 'Branc0', 100, 2, 'gasolina'),
    'pcx': MotoTriciclo('04/12/2022', 'PCX', 'JSW-9323', 14690, 'Azul', 100, 2, 'gasolina')
}

carro = {
    'siena': Carro('12/05/2005', 'Fiat Toro', 'KLE-5785', 37000, 'Vermelho', 200, 'gasolina', 4),
    'uno': Carro('27/03/2022', 'Fiat Uno', 'MRR-1686', 155000, 'Prata', 700, 'gasolina', 4),
    'palio': Carro('12/05/2005', 'Fiat Palio', 'NEX-7345', 23000, 'Preto', 160, 'gasolina', 2),
    'crossfox': Carro('12/05/2005', 'Crossfox', 'MVI-6539', 20000, 'Verde', 300, 'gasolina', 4),
}

camionete = {
    'hilux': Camionete('12/05/2005', 'Hilux 2022', 'MUK-1603', 100000, 450, 'diesel', 4, 20000),
    'fiat_toro': Camionete('12/05/2005', 'Fiat Toro', 'HWN-7280', 130000, 400, 'gasolina', 4, 10000),
    'strada': Camionete('12/05/2005', 'Fiat Strada', 'KIZ-8968', 80000, 350, 'diesel', 4, 10080),
    's10': Camionete('12/05/2005', ' Chevrolet S10', 'MZY-9332', 95000, 400, 'gasolina', 4, 20000),
}

veiculos = {
    'moto_triciclo': moto_triciclo,
    'carro': carro,
    'camionete': camionete
}
