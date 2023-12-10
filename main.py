from datetime import datetime

from bike import RoadBike, MountainBike
from rental import BikeRentalService


def convert_to_date(date):
    return datetime.strptime(date, '%Y-%m-%d')

def start_bike_rent(rental_service):
    start_date = convert_to_date(input(f'Please enter the start date! (yyyy-mm-dd)\n'))
    end_date = convert_to_date(input(f'Please enter the end date! (yyyy-mm-dd)\n'))
    bike_id = input(f'Please enter the bike id\n')

    price = rental_service.rent_a_bike(bike_id, start_date, end_date)

    print(f'-----------------------------------------------------------------------------\n'
          f'Your bike ({bike_id}) has been rented between {start_date} and {end_date}\n'
          f'Total price: {price} HUF\n'
          f'Have a nice day!\n'
          f'-----------------------------------------------------------------------------\n')


def list_rented_bikes(rental_service):
    rental_service.list_all_rented_bikes()


def list_all_bikes(rental_service):
    rental_service.list_all_bikes()


def cancel_rent(rental_service):
    pass


def add_bikes(rental_service):
    rental_service.add_bike(RoadBike('AA254', 3000, 'Good'))
    rental_service.add_bike(RoadBike('BB445', 2000, 'Good'))
    rental_service.add_bike(RoadBike('CC458', 5000, 'Good'))
    rental_service.add_bike(MountainBike('DD545', 6000, 'Good'))
    rental_service.add_bike(MountainBike('GG454', 7000, 'Good'))
    rental_service.add_bike(MountainBike('FF887', 9000, 'Good'))


def create_rents(rental_service):
    rental_service.rent_a_bike('AA254', convert_to_date('2023-07-01'), convert_to_date('2023-07-08'))
    rental_service.rent_a_bike('BB445', convert_to_date('2023-08-04'), convert_to_date('2023-08-16'))
    rental_service.rent_a_bike('CC458', convert_to_date('2023-07-01'), convert_to_date('2023-07-08'))
    rental_service.rent_a_bike('DD545', convert_to_date('2023-06-05'), convert_to_date('2023-06-20'))
    rental_service.rent_a_bike('FF887', convert_to_date('2023-05-10'), convert_to_date('2023-07-18'))


if __name__ == '__main__':
    bike_rental_service = BikeRentalService('GDE Bike Rental')

    add_bikes(bike_rental_service)

    create_rents(bike_rental_service)

    while True:
        selected_option = input(f'Please choose from the options bellow:\n'
                                f'1. Rent a bike\n'
                                f'2. List all bikes\n'
                                f'3. List all rented bikes\n'
                                f'4. Cancel rent\n'
                                f'5. Exit\n')

        if selected_option == '1':
            start_bike_rent(bike_rental_service)
        elif selected_option == '2':
            list_all_bikes(bike_rental_service)
        elif selected_option == '3':
            list_rented_bikes(bike_rental_service)
        elif selected_option == '4':
            cancel_rent(bike_rental_service)
        elif selected_option == '5':
            break
        else:
            print(f'Invalid input')

