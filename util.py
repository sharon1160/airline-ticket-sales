import operator
from collections import Counter


def getTotalTickets(listFlies):
    numTickets = 0
    for fly in listFlies:
        numTickets = numTickets + fly.num_economic_tickets + fly.num_premium_tickets
    return numTickets


def getPlaneWithMaxTickets(listFlies):
    dictFliesTickets = {}
    for fly in listFlies:
        if fly.route.namePlane in dictFliesTickets:
            # update Total
            dictFliesTickets[fly.route.namePlane] = dictFliesTickets[fly.route.namePlane] + \
                fly.num_economic_tickets + fly.num_premium_tickets
        else:
            dictFliesTickets[fly.route.namePlane] = fly.num_economic_tickets + \
                fly.num_premium_tickets
    max_key = max(dictFliesTickets.items(), key=operator.itemgetter(1))[0]
    return max_key


def getIncomeEconomicsTickets(listFlies):
    income_economics_tickets = 0
    for fly in listFlies:
        economic_price = fly.route.base_sale_price + fly.route.economic_seat_price
        income_economics_tickets = income_economics_tickets + \
            fly.num_economic_tickets*economic_price
    return income_economics_tickets


def getIncomePremiumTickets(listFlies):
    income_premium_tickets = 0
    for fly in listFlies:
        premium_price = fly.route.base_sale_price + fly.route.premium_seat_price
        income_premium_tickets = income_premium_tickets + \
            fly.num_economic_tickets*premium_price
    return income_premium_tickets


def getNumberEconomicTickets(listFlies):
    num_economic_tickets = 0
    for fly in listFlies:
        num_economic_tickets = num_economic_tickets + fly.num_economic_tickets
    return num_economic_tickets


def getNumberPremiumTickets(listFlies):
    num_premium_tickets = 0
    for fly in listFlies:
        num_premium_tickets = num_premium_tickets + fly.num_premium_tickets
    return num_premium_tickets


def getFlyMaxTickets(listFlies):
    dictFliesTickets = {}
    for fly in listFlies:
        if fly.route.name_ruta in dictFliesTickets:
            # update Total
            dictFliesTickets[fly.route.name_ruta] = dictFliesTickets[fly.route.name_ruta] + \
                fly.num_economic_tickets + fly.num_premium_tickets
        else:
            dictFliesTickets[fly.route.name_ruta] = fly.num_economic_tickets + \
                fly.num_premium_tickets
    max_key = max(dictFliesTickets.items(), key=operator.itemgetter(1))[0]
    return max_key


def getFlyMinTickets(listFlies):
    dictFliesTickets = {}
    for fly in listFlies:
        if fly.route.name_ruta in dictFliesTickets:
            # update Total
            dictFliesTickets[fly.route.name_ruta] = dictFliesTickets[fly.route.name_ruta] + \
                fly.num_economic_tickets + fly.num_premium_tickets
        else:
            dictFliesTickets[fly.route.name_ruta] = fly.num_economic_tickets + \
                fly.num_premium_tickets
    min_key = min(dictFliesTickets.items(), key=operator.itemgetter(1))[0]
    return min_key


def get3Max(listFlies):
    '''
    dictFliesTickets = {}
    list_max = []
    for fly in listFlies:

        dictFliesTickets[fly.route.name_ruta] = fly.num_economic_tickets(
            fly.route.base_sale_price + fly.route.economic_seat_price) + fly.num_premium_tickets(fly.route.base_sale_price + fly.route.premium_seat_price)

    k = Counter(dictFliesTickets)

    high = k.most_common(3)

    for i in high:
        list_max.append(i[0])

    return list_max'''
    pass
