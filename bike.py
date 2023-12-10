from abc import ABC

ROAD_BIKE = 'ROAD_BIKE'
MOUNTAIN_BIKE = 'MOUNTAIN_BIKE'


class Bike(ABC):
    def __init__(self, bike_id, bike_type, price, condition):
        self._bike_id = bike_id
        self._bike_type = bike_type
        self._price = price
        self._condition = condition

    @property
    def bike_id(self):
        return self._bike_id

    @property
    def bike_type(self):
        return self._bike_type

    @property
    def price(self):
        return self._price

    @property
    def condition(self):
        return self._condition

    def get_bike_info(self):
        return (f'Bike ID: {self._bike_id}\n'
                f'Type: {self._bike_type}\n'
                f'Condition: {self._condition}\n'
                f'Price for a day: {self._price}\n')


class RoadBike(Bike):
    def __init__(self, bike_id, price, condition):
        super().__init__(bike_id, ROAD_BIKE, price, condition)


class MountainBike(Bike):
    def __init__(self, bike_id, price, condition):
        super().__init__(bike_id, MOUNTAIN_BIKE, price, condition)
