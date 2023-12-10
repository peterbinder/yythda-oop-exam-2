from exception import BikeRentalException


class BikeRent:
    def __init__(self, bike, start_date, end_date):
        self._id = f'{bike.id}-{start_date}-{end_date}'
        self._bike = bike
        self._start_date = start_date
        self._end_date = end_date

class BikeRentalService:
    def __init__(self, name):
        self._name = name
        self._bikes = []
        self._bike_rentals = []

    def rent_a_bike(self, bike_id, start_date, end_date):
        if self.bike_is_available(bike_id, start_date, end_date):
            bike = self.find_bike_by_id(bike_id)
            rent = BikeRent(bike, start_date, end_date)

    def bike_is_available(self, bike_id, start_date, end_date):
        pass

    def does_bike_exist(self, bike_id):
        pass

    def find_bike_by_id(self, bike_id):
        for bike in self._bikes:
            if bike.bike_id == bike_id:
                return bike
        raise BikeRentalException('Bike is not found')