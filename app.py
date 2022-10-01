from typing import List, Dict, Tuple
from model.Fly import Fly
from model.Route import Route
import random
from config import IGV_PERCENT, CURRENCY_SYMBOL
from colorama import Style, Back, Fore, init

from util import *




def create_list_routes() -> List[Route]:
    """
    Función que crea y devuelve una lista de objetos Route
    """
    data_routes: List[Dict[str, str | float | int | tuple]] = [
        {
            "cod_ruta": "LIM - AYA",
            "name_ruta": "LIMA - AYACUCHO",
            "base_sale_price": 55.19,
            "economic_seat_price": 8.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (120, 130),
            "ticket_premium_num_range": (10, 20),
            "namePlane": "A001"
        },
        {
            "cod_ruta": "LIM - CUS",
            "name_ruta": "LIMA - CUSCO",
            "base_sale_price": 136.51,
            "economic_seat_price": 8.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (130, 144),
            "ticket_premium_num_range": (15, 24),
            "namePlane": "A002"
        },
        {
            "cod_ruta": "LIM - ARE",
            "name_ruta": "LIMA - AREQUIPA",
            "base_sale_price": 90.59,
            "economic_seat_price": 8.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (115, 138),
            "ticket_premium_num_range": (16, 22),
            "namePlane": "A003"
        },
        {
            "cod_ruta": "LIM - TAR",
            "name_ruta": "LIMA - TARAPOTO",
            "base_sale_price": 71.89,
            "economic_seat_price": 8.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (100, 120),
            "ticket_premium_num_range": (12, 18),
            "namePlane": "A004"
        },
        {
            "cod_ruta": "AYA - LIM",
            "name_ruta": "AYACUCHO - LIMA",
            "base_sale_price": 40.42,
            "economic_seat_price": 7.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (100, 115),
            "ticket_premium_num_range": (10, 15),
            "namePlane": "A001"
        },
        {
            "cod_ruta": "CUS - LIM",
            "name_ruta": "CUSCO - LIMA",
            "base_sale_price": 124.32,
            "economic_seat_price": 7.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (105, 120),
            "ticket_premium_num_range": (14, 20),
            "namePlane": "A002"
        },
        {
            "cod_ruta": "ARE - LIM",
            "name_ruta": "AREQUIPA - LIMA",
            "base_sale_price": 86.59,
            "economic_seat_price": 7.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (100, 110),
            "ticket_premium_num_range": (13, 18),
            "namePlane": "A003"
        },
        {
            "cod_ruta": "TAR - LIM",
            "name_ruta": "TARAPOTO - LIMA",
            "base_sale_price": 68.42,
            "economic_seat_price": 7.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (90, 105),
            "ticket_premium_num_range": (10, 15),
            "namePlane": "A004"
        }
    ]

    # Lista de objetos Route
    routes: List[Route] = []

    # Iteramos la lista de rutas
    for key, route in enumerate(data_routes):
        # Creamos el objeto ruta
        obj_route = Route(str(route['cod_ruta']), str(route['name_ruta']), float(route['base_sale_price']), float(route['economic_seat_price']), float(
            route['premium_seat_price']), tuple(route['ticket_econ_num_range']), tuple(route['ticket_premium_num_range']), str(route['namePlane']))
        routes.append(obj_route)
    return routes


def create_list_flies(routes) -> List[Fly]:

    # Lista de objetos Fly
    flies: List[Fly] = []

    for route in routes:
        num_tickets_economics: int = random.randint(
            route.ticket_econ_num_range[0], route.ticket_econ_num_range[1])
        num_tickets_premium: int = random.randint(
            route.ticket_premium_num_range[0], route.ticket_premium_num_range[1])
        obj_fly = Fly(route, num_tickets_economics, num_tickets_premium)
        flies.append(obj_fly)
    return flies


def main():

    # Crear la lista de objetos Route
    routes: List[Route] = create_list_routes()

    # Crear la lista de objetos Fly
    flies: List[Fly] = create_list_flies(routes)

    # Llamar a las funciones de util
    income_total_economics: float = getIncomeEconomicsTickets(flies)
    income_total_premium: float = getIncomePremiumTickets(flies)
    total_IGV: float = (income_total_economics +
                        income_total_premium)*IGV_PERCENT/100
    number_economic_tickets: int = getNumberEconomicTickets(flies)
    number_premium_tickets: int = getNumberPremiumTickets(flies)
    total_tickets: int = number_economic_tickets + number_premium_tickets
    average_value_economic: float = (IGV_PERCENT/100 + 1) * \
        income_total_economics / number_economic_tickets
    average_value_premium: float = (IGV_PERCENT/100 + 1) * \
        income_total_premium / number_premium_tickets
    fly_max_value: str = getFlyMaxTickets(flies)
    fly_min_value: str = getFlyMinTickets(flies)
    three_fly_max: list = get3Max(flies)
    fly_max_tickets: str = getPlaneWithMaxTickets(flies)

    # Llamar a la función init() de colorama
    init()
    print("======================================")
    print(f"{Back.RED}{Fore.WHITE}VUELOS{Back.RESET}{Fore.RESET}")
    print("======================================")

    for fly in flies:
        print(Back.WHITE + Fore.CYAN)
        print(f"Cod. Ruta: {fly.route.cod_ruta}")
        print(f"Ruta: {fly.route.name_ruta}")
        print(f"Número de ventas Económico: {fly.num_economic_tickets}")
        print(f"Número de ventas Premium: {fly.num_premium_tickets}")
        economic_cost = fly.route.base_sale_price + fly.route.economic_seat_price
        print(
            f"Costo económico por venta unitaria: {get_currency_format(CURRENCY_SYMBOL,round(economic_cost,2))}")
        premium_cost = fly.route.base_sale_price + fly.route.premium_seat_price
        print(
            f"Costo premium por venta unitaria: {get_currency_format(CURRENCY_SYMBOL,round(premium_cost,2))}")
        subtotal = fly.num_economic_tickets*economic_cost + \
            fly.num_premium_tickets*premium_cost
        print(
            f"SUBTOTAL: {get_currency_format(CURRENCY_SYMBOL,round(subtotal,2))}")
        igv = IGV_PERCENT/100*subtotal
        print(f"IGV: {get_currency_format(CURRENCY_SYMBOL,round(igv,2))}")
        Total = (IGV_PERCENT/100+1)*subtotal
        print(f"TOTAL: {get_currency_format(CURRENCY_SYMBOL,round(Total,2))}")
        print(Back.RESET + Fore.RESET)
        print("======================================")

    print(f"{Back.RED}{Fore.WHITE}RESPUESTAS{Back.RESET}{Fore.RESET}")
    print("======================================")

    color_on = Fore.GREEN
    color_off = Fore.RESET

    print(
        f"El total de pasajes vendidos entre todos los vuelos: {color_on}{str(total_tickets)}{color_off}")
    print(
        f"El total de ingresos por la venta de pasajes económicos: {color_on}{get_currency_format(CURRENCY_SYMBOL,round(income_total_economics, 2))}{color_off}")
    print(
        f"El total de ingresos por la venta de pasajes premium: {color_on}{get_currency_format(CURRENCY_SYMBOL,round(income_total_premium, 2))}{color_off}")
    print(
        f"El importe total de IGV cobrado es: {color_on}{get_currency_format(CURRENCY_SYMBOL,round(total_IGV, 2))}{color_off}")
    print(
        f"El valor promedio de un pasaje económico es: {color_on}{get_currency_format(CURRENCY_SYMBOL,round(average_value_economic, 2))}{color_off}")
    print(
        f"El valor promedio de un pasaje premium es: {color_on}{get_currency_format(CURRENCY_SYMBOL,round(average_value_premium, 2))}{color_off}")
    print(
        f"El vuelo con la mayor cantidad de pasajeros es: {color_on}{fly_max_value}{color_off}")
    print(
        f"El vuelo con la menor cantidad de pasajeros es: {color_on}{fly_min_value}{color_off}")
    print(
        f"Los tres primeros vuelos que obtuvieron los mayores ingresos por la venta de asientos son: {color_on}{three_fly_max[0]}, {three_fly_max[1]}, {three_fly_max[2]}{color_off}")
    print(
        f"El avion que transporto más pasajeros fue: {color_on}{fly_max_tickets}{color_off}")


if __name__ == "__main__":
    main()
