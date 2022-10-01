from model.Fly import Fly
from model.Route import Route
import random

from util import *


def main():

    # los datos de las rutas deberian jañarse de un archivo config, buscar una forma ordenada
    route1: Route = Route("LIM - AYA", "LIMA - AYACUCHO ",
                          55.19, 8, 16, (120, 130), (10, 20), "A001")
    route2: Route = Route("LIM - CUS", "LIMA - CUSCO ",
                          136.51, 8, 16, (130, 144), (15, 24), "A002")

    list1: list = [route1, route2]
    listFlies: list = []

    for route in list1:
        print(route.cod_ruta)
        fly1: Fly = Fly(route, random.randint(route.ticket_econ_num_range[0], route.ticket_econ_num_range[1]), random.randint(
            route.ticket_premium_num_range[0], route.ticket_premium_num_range[1]))
        listFlies.append(fly1)
    print("Debo tener 2 vuelos")

    # aca el problema es: dada una lista de vuelos... hallar las preguntas
    total_tickets = getTotalTickets(listFlies)
    income_total_economics = getIncomeEconomicsTickets(listFlies)
    income_total_premium = getIncomePremiumTickets(listFlies)
    total_IGV = (income_total_economics + income_total_premium)*0.18
    number_economic_tickets = getNumberEconomicTickets(listFlies)
    number_premium_tickets = getNumberPremiumTickets(listFlies)
    total = number_economic_tickets + number_premium_tickets
    average_value_economic: float = 1.18 * \
        income_total_economics/number_economic_tickets
    average_value_premium: float = 1.18*income_total_premium/number_premium_tickets
    fly_max_value = getFlyMaxTickets(listFlies)
    fly_min_value = getFlyMinTickets(listFlies)
    three_fly_max: list = get3Max(listFlies)
    fly_max_tickets = getPlaneWithMaxTickets(listFlies)

    print("El total de pasajes vendidos entre todos los vuelos: " +
          str(total_tickets) + "=" + str(total))
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
