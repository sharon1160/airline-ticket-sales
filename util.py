import operator
from collections import Counter


def get_plane_with_max_tickets(listFlies) -> str:
    """
    Método para obtener el avión que transportó la mayor cantidad de pasajeros
    """
    dictFliesTickets:  dict = {}
    for fly in listFlies:
        if fly.route.name_plane in dictFliesTickets:
            # update Total
            dictFliesTickets[fly.route.name_plane] = dictFliesTickets[fly.route.name_plane] + \
                fly.num_economic_tickets + fly.num_premium_tickets
        else:
            dictFliesTickets[fly.route.name_plane] = fly.num_economic_tickets + \
                fly.num_premium_tickets
    max_key = max(dictFliesTickets.items(), key=operator.itemgetter(1))[0]
    return max_key


def get_income_economics_tickets(listFlies) -> float:
    """
    Método para obtener los ingresos por las ventas de pasajes económicos (sin IGV)
    """
    income_economics_tickets = 0
    for fly in listFlies:
        economic_price = fly.route.base_sale_price + fly.route.economic_seat_price
        income_economics_tickets = income_economics_tickets + \
            fly.num_economic_tickets*economic_price
    return income_economics_tickets


def get_income_premium_tickets(listFlies) -> float:
    """
    Método para obtener los ingresos por las ventas de pasajes premium (sin IGV)
    """
    income_premium_tickets = 0
    for fly in listFlies:
        premium_price = fly.route.base_sale_price + fly.route.premium_seat_price
        income_premium_tickets = income_premium_tickets + \
            fly.num_economic_tickets*premium_price
    return income_premium_tickets


def get_number_economic_tickets(listFlies) -> int:
    """
    Método para obtener número de tickets económicos vendidos
    """
    num_economic_tickets = 0
    for fly in listFlies:
        num_economic_tickets = num_economic_tickets + fly.num_economic_tickets
    return num_economic_tickets


def get_number_premium_tickets(listFlies) -> int:
    """
    Método para obtener número de tickets premium vendidos
    """
    num_premium_tickets = 0
    for fly in listFlies:
        num_premium_tickets = num_premium_tickets + fly.num_premium_tickets
    return num_premium_tickets


def get_fly_max_tickets(listFlies) -> str:
    """
    Método para obtener el vuelo con la mayor cantidad de pasajeros
    """
    dictFliesTickets = {}
    for fly in listFlies:
        dictFliesTickets[fly.route.name_ruta] = fly.num_economic_tickets + \
            fly.num_premium_tickets
    max_key = max(dictFliesTickets.items(), key=operator.itemgetter(1))[0]
    return max_key


def get_fly_min_tickets(listFlies) -> str:
    """
    Método para obtener el vuelo con la menor cantidad de pasajeros
    """
    dictFliesTickets = {}
    for fly in listFlies:
        dictFliesTickets[fly.route.name_ruta] = fly.num_economic_tickets + \
            fly.num_premium_tickets
    temp = min(dictFliesTickets.values())
    min_key = [key for key in dictFliesTickets if dictFliesTickets[key] == temp]
    return min_key[0]


def get3Max(listFlies) -> list:
    """
    Método para obtener una lista con los 3 primeros vuelos que tuvieron mayores ingresos
    """
    dictFliesTickets = {}
    list_max = []
    for fly in listFlies:
        dictFliesTickets[fly.route.name_ruta] = fly.num_economic_tickets*(
            fly.route.base_sale_price + fly.route.economic_seat_price) + fly.num_premium_tickets*(fly.route.base_sale_price + fly.route.premium_seat_price)

    k = Counter(dictFliesTickets)
    high = k.most_common(3)

    for i in high:
        list_max.append(i[0])

    return list_max


def get_currency_format(currency_symbol, amount) -> str:
    """
    Método para formatear una variable numérica en string con formato de moneda
    """
    return "{}{:,.2f}".format(currency_symbol, amount)
