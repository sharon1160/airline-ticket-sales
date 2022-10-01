from typing import Tuple


class Route(object):
    def __init__(self, cod_ruta: str, name_ruta: str, base_sale_price: float, economic_seat_price: float, premium_seat_price: float, ticket_econ_num_range: tuple[int, int], ticket_premium_num_range: tuple[int, int], name_plane: str):
        """
        Constructor de la clase Route
        """
        self.cod_ruta: str = cod_ruta
        self.name_ruta: str = name_ruta
        self.base_sale_price: float = base_sale_price
        self.economic_seat_price: float = economic_seat_price
        self.premium_seat_price: float = premium_seat_price
        self.ticket_econ_num_range: tuple[int, int] = ticket_econ_num_range
        self.ticket_premium_num_range: tuple[int,
                                             int] = ticket_premium_num_range
        self.name_plane: str = name_plane
