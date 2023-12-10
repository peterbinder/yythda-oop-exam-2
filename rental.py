from exception import BikeRentalException


class RentalItem:
    def __init__(self, bike, start_date, end_date):
        self._rent_id = f'{bike.id}-{start_date}-{end_date}'
        self._bike = bike
        self._start_date = start_date
        self._end_date = end_date

    @property
    def rent_id(self):
        return self._rent_id

    @property
    def bike(self):
        return self._bike

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    def get_price(self):
        return self._bike.price * (self._end_date - self._start_date)


class BikeRentalService:
    def __init__(self, name):
        self._name = name
        self._bikes = []
        self._rental_list = []

    def rent_a_bike(self, bike_id, start_date, end_date):
        if self.is_bike_available(bike_id, start_date, end_date):
            bike = self.find_bike(bike_id)
            rental = RentalItem(bike, start_date, end_date)
            self._rental_list.append(rental)
            return rental.get_price()

        raise BikeRentalException('Bike is not available in the given period'
                                  '')

    def is_bike_available(self, bike_id, start_date, end_date):
        for rental_item in self._rental_list:
            if rental_item.bike.bike_id == bike_id and rental_item.end_date >= start_date and rental_item.start_date <= end_date:
                return False
            return True

    def does_bike_exist(self, bike_id):
        pass

    def find_bike(self, bike_id):
        for bike in self._bikes:
            if bike.bike_id == bike_id:
                return bike
        raise BikeRentalException('Bike is not found')
