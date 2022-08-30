"""Route planning file

A file for demonstrate a navigation process scenario of a driverless car.
It has a text-based user interface where the user is prompted 
to make the appropriate entries.
"""

class GPS:
    """GPS class

    A class for executing the current position of the driverless car.
    
    Attributes: 
        current_position (str): Current position of the driverless Car.
    """

    def __init__(self, current_position):
        """Inits GPS class"""
        self.current_position = current_position

    def driverless_car_position(self):
        """Method for printing the current posotion of the driverless car."""

        print(f'Your current position is {self.current_position}')

class Navigation(GPS):
    """Navigation class
    
    A subcluss of GPS with the functions of a navigation system.
    
    Attributes:
        current_position (str): Current position of the driverless Car.
        route: Information about the route (Component class Route).
        final_destination (str): Empty string.
        destination (list): The List of all destinations.
    """

    def __init__(self, current_position, route):
        """Inits Navigation class."""

        self.current_position = current_position
        self.route = route
        self.final_destination = ' '
        self.destination = []

    def add_destination(self):
        """Method for adding new destinations to the destination list.
        
        Return:
            destination: Destination list.
        """

        new_destination = input('Enter your destination: ').capitalize()
        self.destination.append(new_destination)
        return self.destination
    
    def show_destination_list(self):
        """Method for printing the destination list as a string."""

        for index, info in enumerate(self.destination):
            print(f"{index + 1}) {info.capitalize()}")

    def search_destination(self):
        """Method for searching for the final destination.
        
        Return:
            final_destination: Assigned a destination to the variable.
        """

        self.add_destination()
        self.final_destination = self.destination[-1]
        return self.final_destination

    def get_final_destintion(self):
        """Method for printing the final destiantion."""

        print(self.final_destination)
    
    def update_destination(self):
        """Method for updating the destination list.
        
        Return:
            final_destination: Return the final destination.
        """

        self.destination.pop()
        self.search_destination()
        return self.final_destination

    def delete_destination(self):
        """Method for deleting the last destination of the destinarion list.
        
        Return:
            destination: Return the destination list.
        """

        self.destination.pop()
        print('Your last record is deleted')
        return self.destination

class Route:
    """Route class
    
    A component class for calculating and printing the route for the navigation class.
    
    Attributes:
        distance (int): Distance in km, assigned to 0.
        time (int): Time in hour, assigned to 0.
    """

    def __init__(self):
        """Inits Route class."""

        self.distance = 0
        self.time = 0

    def calculate_route(self, navigation):
        """Method for calculating the route of the current position to the final destination.
        
        Parameter: 
            navigation: Information from navigation class (current_position, final_destination).
        
        Return:
            True: Input of user was true and the calculation was successful.
            Method calculate_route: Execute the method again if an incorrect entry was made.
        """

        print(f'Calculation route from {navigation.current_position} to {navigation.final_destination} \n')
        self.distance = input('Enter the distance in km between your current position and your destination: ')
        try:       #handling exception (only integers)
            self.time = int(self.distance)/100
            print(f'\nThe distance is {self.distance}km')
            print(f'With an average speed of 100 km/h, the journey takes: {self.time}h \n')
            return True
        except:
            print('Input wrong! Only intergers, try again \n')
            return self.calculate_route(navigation)

    def show_route(self, navigation):
        """Method for printing the route.
        
        Parameter: 
            navigation: Information from navigation class (current_position, final_destination).
        """

        print(f'Current Position: {navigation.current_position} \nDestination: {navigation.final_destination}')
        print(f'Distance: {self.distance}km \nTime: {self.time}h \n')

    def start_navigation(self, navigation):
        """"Method for starting the navigation or cancel the route.
        
        Parameter: 
            navigation: Information from navigation class (current_position, final_destination).
        
        Return:
            start: Starting the navigation.
            cancel: Cancel the route and delete the destination.
            Method start_navigation: Execute the method again if an incorrect entry was made.
        """
        
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
        """Method for executing route info from obstacle classes."""

        obsctacle.route_info()

def main():
    """Main function to create the objects and execute the file."""

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

