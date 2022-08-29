class GPS:
    def __init__(self, current_position):
        self.current_position = current_position

    def driverless_car_position(self):
        print(f'Your current position is {self.current_position}')

class Navigation(GPS):

    def __init__(self, current_position, route):
        self.current_position = current_position
        self.route = route
        self.final_destination = ' '
        self.destination = []

    def add_destination(self):
        new_destination = input('Enter your destination: ').capitalize()
        self.destination.append(new_destination)
        return self.destination
    
    def show_destination_list(self):
        for index, info in enumerate(self.destination):
            print(f"{index + 1}) {info.capitalize()}")

    def search_destination(self):
        self.add_destination()
        self.final_destination = self.destination[-1]
        return self.final_destination

    def get_final_destintion(self):
        print(self.final_destination)
    
    def update_destination(self):
        self.destination.pop()
        self.search_destination()
        return self.final_destination

    def delete_destination(self):
        self.destination.pop()
        print('Your last record is deleted')
        return self.destination

class Route:

    def __init__(self):
        self.distance = 0
        self.time = 0

    def calculate_route(self, navigation):
        print(f'Calculation route from {navigation.current_position} to {navigation.final_destination} \n')
        self.distance = input('Enter the distance in km between your current position and your destination: ')
        try:
            self.time = int(self.distance)/100
            print(f'\nThe distance is {self.distance}km')
            print(f'With an average speed of 100 km/h, the journey takes: {self.time}h \n')
            return True
        except:
            print('Input wrong! Only intergers, try again \n')
            return self.calculate_route(navigation)

    def show_route(self, navigation):
        print(f'Current Position: {navigation.current_position} \nDestination: {navigation.final_destination}')
        print(f'Distance: {self.distance}km \nTime: {self.time}h \n')

    def start_navigation(self, navigation):
        confirm = input('(A)ccept route \n(C)ancel route \n> ').lower()
        if confirm == 'a':
            print('Starting navigation')
            return 'start'
        elif confirm == 'c':
            navigation.delete_destination()
            return 'cancel'
        else:
            print('Input wrong! try again \n')
            return self.start_navigation()

    def route_information(self, obsctacle):
        obsctacle.route_info()

def main():
    route = Route()
    navi = Navigation('Wolfsburg', route)

    print('Route Planning Scenario')
    print('Starting navigation sytem \n')
    navi.driverless_car_position()

    print('\nTo start your journey, add a destination you want to travel to \n')
    navi.search_destination()

    print('\nYour destination list:')
    navi.show_destination_list()

    print('\nYou wish to delete the last entry')
    navi.delete_destination()

    print('\nShowing map:')
    navi.driverless_car_position()

    print('\nSearch again and add a destination you want to travel to')
    navi.search_destination()

    print('\nYour destination list:')
    navi.show_destination_list()

    print('\nUpdate your destination')
    navi.update_destination()

    print('\nYour new destination list:')
    navi.show_destination_list()

    print('\nDue to the stacking order (last in, first out)', end=' ')
    print('the last destination is removed and a new destination is added at the top \n')

    print('Now start the route:')
    navi.route.calculate_route(navi)
    navi.route.show_route(navi)
    navi.route.start_navigation(navi)

if __name__ == '__main__':
    main()

