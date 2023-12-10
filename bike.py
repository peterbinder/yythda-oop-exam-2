from abc import ABC

ROAD_BIKE = 'ROAD_BIKE'
MOUNTAIN_BIKE = 'MOUNTAIN_BIKE'


class Bike(ABC):
    def __init__(self, bike_type, price, condition):
        self._bike_type = bike_type
        self._price = price
        self._condition = condition


class RoadBike(Bike):
    def __init__(self, price, condition):
        super().__init__(ROAD_BIKE, price, condition)

    @property
    def bike_type(self):
        return self._bike_type

    @property
    def price(self):
        return self._price

    @property
    def condition(self):
        return self._condition


class MountainBike(Bike):
    def __init__(self, price, condition):
        super().__init__(MOUNTAIN_BIKE, price, condition)

    @property
    def bike_type(self):
        return self._bike_type

    @property
    def price(self):
        return self._price

    @property
    def condition(self):
        return self._condition