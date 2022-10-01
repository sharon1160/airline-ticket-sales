from typing import List, Dict
from model.Fly import Fly
from model.Route import Route
import random

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
            "namePlane": "A001",
        },
        {
            "cod_ruta": "LIM - CUS",
            "name_ruta": "LIMA - CUSCO",
            "base_sale_price": 136.51,
            "economic_seat_price": 8.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (130, 144),
            "ticket_premium_num_range": (15, 24),
            "namePlane": "A002",
        },
        {
            "cod_ruta": "LIM - ARE",
            "name_ruta": "LIMA - AREQUIPA",
            "base_sale_price": 90.59,
            "economic_seat_price": 8.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (115, 138),
            "ticket_premium_num_range": (16, 22),
            "namePlane": "A003",
        },
        {
            "cod_ruta": "LIM - TAR",
            "name_ruta": "LIMA - TARAPOTO",
            "base_sale_price": 71.89,
            "economic_seat_price": 8.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (100, 120),
            "ticket_premium_num_range": (12, 18),
            "namePlane": "A004",
        },
        {
            "cod_ruta": "AYA - LIM",
            "name_ruta": "AYACUCHO - LIMA",
            "base_sale_price": 40.42,
            "economic_seat_price": 7.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (100, 115),
            "ticket_premium_num_range": (10, 15),
            "namePlane": "A001",
        },
        {
            "cod_ruta": "CUS - LIM",
            "name_ruta": "CUSCO - LIMA",
            "base_sale_price": 124.32,
            "economic_seat_price": 7.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (105, 120),
            "ticket_premium_num_range": (14, 20),
            "namePlane": "A002",
        },
        {
            "cod_ruta": "ARE - LIM",
            "name_ruta": "AREQUIPA - LIMA",
            "base_sale_price": 86.59,
            "economic_seat_price": 7.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (100, 110),
            "ticket_premium_num_range": (13, 18),
            "namePlane": "A003",
        },
        {
            "cod_ruta": "TAR - LIM",
            "name_ruta": "TARAPOTO - LIMA",
            "base_sale_price": 68.42,
            "economic_seat_price": 7.00,
            "premium_seat_price": 16.00,
            "ticket_econ_num_range": (90, 105),
            "ticket_premium_num_range": (10, 15),
            "namePlane": "A004",
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
    flies: List[fly] = []

    for route in routes:
        obj_fly: Fly = Fly(route, random.randint(route.ticket_econ_num_range[0], route.ticket_econ_num_range[1]), random.randint(
            route.ticket_premium_num_range[0], route.ticket_premium_num_range[1]))
        flies.append(obj_fly)
    return flies


def main():

    # Crear la lista de objetos Route
    routes: List[Route] = create_list_routes()

    # Crear la lista de objetos Fly
    flies: List[Route] = create_list_flies(routes)

    # aca el problema es: dada una lista de vuelos... hallar las preguntas
    total_tickets = getTotalTickets(flies)
    income_total_economics = getIncomeEconomicsTickets(flies)
    income_total_premium = getIncomePremiumTickets(flies)
    total_IGV = (income_total_economics + income_total_premium)*0.18
    number_economic_tickets = getNumberEconomicTickets(flies)
    number_premium_tickets = getNumberPremiumTickets(flies)
    total = number_economic_tickets + number_premium_tickets
    average_value_economic: float = 1.18 * \
        income_total_economics/number_economic_tickets
    average_value_premium: float = 1.18*income_total_premium/number_premium_tickets
    fly_max_value = getFlyMaxTickets(flies)
    fly_min_value = getFlyMinTickets(flies)
    three_fly_max: list = get3Max(flies)
    fly_max_tickets = getPlaneWithMaxTickets(flies)

    print("El total de pasajes vendidos entre todos los vuelos: " +
          str(total_tickets))
    print("El total de ingresos por la venta de pasajes económicos: " +
          str(income_total_economics))
    print("El total de ingresos por la venta de pasajes económicos: " +
          str(income_total_premium))
    print("El importe total de IGV cobrado es: " + str(total_IGV))
    print("El valor promedio de un pasaje económico es: " +
          str(average_value_economic))
    print("El valor promedio de un pasaje premium es: " +
          str(average_value_premium))
    print("El vuelo con la mayor cantidad de pasajeros es: " + fly_max_value)
    print("El vuelo con la menor cantidad de pasajeros es: " + fly_min_value)
    # print("Los tres primeros vuelos que obtuvieron los mayores ingresos por la venta de asientos son: " +
    #      three_fly_max[0]+","+three_fly_max[1]+","+three_fly_max[2])
    print("El avion que transporto mas pasajeros fue: " + fly_max_tickets)


if __name__ == "__main__":
    main()
