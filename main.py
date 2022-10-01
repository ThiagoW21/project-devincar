from tinydb import TinyDB

from variables.veiculos import veiculos

db = TinyDB("db.json")


stop = False


def show_vehicle(option_of_vehicle, vehicle_type):
    while True:
        print(f'\n{"Informações do veículo":-^50}\n')

        vehicles = veiculos[vehicle_type]

        keys = [key for key in vehicles.keys() if key != "Voltar"]

        data_vehicle = vehicles[keys[option_of_vehicle]].data_vehicle

        for key, value in data_vehicle.items():
            print(f'    {key.replace("_", " ").upper()}: {value}')

        print(
            (
                f"""
                    [1] - Editar cor {"- indisponível" if vehicle_type == 'camionete' else ''}
                    [2] - Editar preço
                    [3] - Vender
                    [4] - Menu anterior
                    """
            )
        )

        try:
            vehicle_options = int(input("\nOpção: "))
        except ValueError:
            print("\nDigite uma opção válida!")
            continue

        while (
            vehicle_options == 1
            and vehicle_type == "camionete"
            or vehicle_options not in [1, 2, 3, 4]
        ):
            try:
                vehicle_options = int(input("\nOpção inválida, tente novamente: "))

            except ValueError:
                continue

        vehicle = vehicles[keys[option_of_vehicle]]

        if vehicle_options == 1 and vehicle_type != "camionete":
            color = input("Cor: ")

            while len(color) < 3:
                color = input("Cor inválida, tente novamente: ")

            vehicle.color = color
            continue

        elif vehicle_options == 2:
            price = float(input("Preço: "))

            while price <= 0:
                price = float(
                    input("Preço precisa ser maior que zero, tente novamente: ")
                )

            vehicle.price = price
            continue

        elif vehicle_options == 3:
            cpf_buyer = input("\nCPF do comprador: ")

            while len(cpf_buyer) != 11:
                cpf_buyer = (
                    input("\nCPF precisa ter 11 dígitos: ")
                    .replace(".", "")
                    .replace("-", "")
                )

            vehicle.cpf_buyer = cpf_buyer

            vehicle.sell_vehicle()

            continue

        elif vehicle_options == 4:
            return


def list_vehicles_of_type(vehicle_type):
    while True:
        print(f'\n{"Listando veículos por categoria":-^50}\n')
        print("Escolha um veículo para visualizar detalhes")

        vehicles = veiculos[vehicle_type]

        index = 1

        for key, value in vehicles.items():
            print(f'    [{index}] - {key.replace("_", " ").title()}')
            index += 1

        print(f"    [{index + 1}] - Voltar")

        try:
            option_of_vehicle = int(input("\nOpção: ")) - 1

            while option_of_vehicle > index:
                option_of_vehicle = (
                    int(input("\nOpção inválida, tente novamente: ")) - 1
                )

        except ValueError:
            print("\nDigite uma opção válida!")
            continue

        if option_of_vehicle < 4:
            show_vehicle(option_of_vehicle, vehicle_type)

        else:
            return


def list_all_vehicles(avaiable=False, solds=False):
    for vehicle_type, vehicles in veiculos.items():
        print(f'{"":-^50}')
        print(f'{vehicle_type.replace("_", " ").upper() + "S": ^50}')
        print(f'{"":-^50}')

        for key, vehicle in vehicles.items():
            if avaiable and not vehicle.sold:
                print(f'    {key.replace("_", " ").upper()}')

            elif not avaiable and solds and vehicle.sold:
                print(f'    {key.replace("_", " ").upper()}')

            elif not avaiable and not solds:
                print(f'    {key.replace("_", " ").upper()}')


def list_sales():
    global stop

    prices = [sale["preco"] for sale in db]

    print(f'\n{"Listar vendas":-^50}\n')

    def print_option(len_options):
        while True:
            try:
                option = int(input("\nOpção: "))
                print("")

                while option not in range(1, len_options):
                    option = int(input("\nOpção inválida, tente novamente: "))

                return option

            except ValueError:
                print("\nDigite um valor válido!")
                continue

    while True:
        print(
            """
            [1] - Todas
            [2] - Maior preço
            [3] - Menor preço
            [4] - Voltar
            [5] - Encerrar programa
        """
        )

        option_filter = print_option(6)

        if option_filter == 1:
            for sale in db.all():
                print(f'{"":-^50}')

                for key, value in sale.items():
                    print(f'{key.replace("_", " ").upper()}: {value}')

                print(f'{"":-^50}')

        elif option_filter == 2:
            max_sale = [sale for sale in db if sale["preco"] == max(prices)]

            print(f'{"":-^50}')

            for key, value in max_sale[0].items():
                print(f'{key.replace("_", " ").upper()}: {value}')

            print(f'{"":-^50}')

        elif option_filter == 3:
            min_sale = [sale for sale in db if sale["preco"] == min(prices)]

            print(f'{"":-^50}')

            for key, value in min_sale[0].items():
                print(f'{key.replace("_", " ").upper()}: {value}')

            print(f'{"":-^50}')

        elif option_filter == 4:
            break

        elif option_filter == 5:
            stop = True
            break

        else:
            continue


def show_options_list():
    global stop

    while True:
        print(f'{"Tipos de veículos":-^50}')

        print(
            (
                """
        [1] - Moto/Triciclo
        [2] - Carros
        [3] - Camionete
        [4] - Todos
        [5] - Veículos disponiveis
        [6] - Veículos vendidos
        [7] - Voltar
        [8] - Encerrar programa
        """
            )
        )

        try:
            option_of_type = int(input("Opção: "))

            while option_of_type not in range(1, 9):
                option_of_type = int(input("Opção inválida, tente novamente: "))

        except ValueError:
            print("\nDigite uma opção válida!")
            continue

        if option_of_type == 1:
            list_vehicles_of_type("moto_triciclo")
            continue

        if option_of_type == 2:
            list_vehicles_of_type("carro")
            continue

        elif option_of_type == 3:
            list_vehicles_of_type("camionete")
            continue

        elif option_of_type == 4:
            list_all_vehicles()
            continue

        elif option_of_type == 5:
            list_all_vehicles(True)
            continue

        elif option_of_type == 6:
            list_all_vehicles(solds=True)
            continue

        elif option_of_type == 7:
            break

        elif option_of_type == 8:
            stop = True
            return

        else:
            print("\nDigite uma opção válida!")
            continue


def initial_menu():
    while True:
        print(f'\n{"DEVinCar":-^50}')

        print(
            (
                """
            [1] - Listar veículos
            [2] - Histórico de vendas
            [3] - Encerrar programa
            """
            )
        )

        try:
            option = int(input("Opção: "))

        except ValueError:
            print("\nDigite uma opção válida!")
            continue

        if option == 1:
            show_options_list()

            if stop:
                break

            continue

        elif option == 2:
            list_sales()

            if stop:
                break

            continue

        elif option == 3:
            break

        else:
            print("\nDigite uma opção válida!")
            continue


if __name__ == "__main__":
    initial_menu()
