from model.Route import Route


class Fly(object):
    def __init__(self, route: Route, num_economic_tickets: int, num_premium_tickets: int):
        """
        Constructor de la clase Fly
        """
        self.route: Route = route
        self.num_economic_tickets: int = num_economic_tickets
        self.num_premium_tickets: int = num_premium_tickets
