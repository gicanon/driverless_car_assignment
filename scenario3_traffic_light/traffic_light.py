"""Traffic light file


A file for demonstrate a traffic light scenario.
"""


class Driverless_Car:
    """Driverless car class
    
    A class to specify the model and make of the driverless car.
    
    Attributes:
        brand (str): Brand name of the driverless car.
        model (str): The model of the driverless car.
    """

    def __init__(self, brand, model):
        """Inits the Driverless Car class."""
        self.brand = brand
        self.model = model
            

class Obstacle:
    """Obstacle class
    
    An Abstract class for any obstacles.
    
    Attributes:
        time (int): Time in hour (h).
        speed (int): Speed in km/h.
        distance (int): Distance in km.
        id (int): Unique id for the obstacles.
    """

    def __init__(self, time, speed, distance, id = None):
        """Inits Obstacle class."""

        self.time = time
        self.speed = speed
        self.distance = distance
        self.id = id

class Traffic_light(Obstacle):
    """Traffic light class
    
    A subclass of obstacles.
    
    Attributes:
        colour (str): The dectected traffic light colour."""
    

    def __init__(self, time, speed, distance, colour):
        """Inits Traffic light class."""

        super().__init__(time, speed, distance)
        self.colour = colour

    def __repr__(self):
        """Represent class object as a string."""

        return f'Traffic_Light({self.time}h, {self.speed}km/h, {self.distance}km)' 

    def route_info(self):
        """Method for printing a traffic light message."""

        print('Traffic light is incoming')

    def get_traffic_light_colour(self):
        """Method for returning the colour of the traffic light."""

        return self.colour

    def detect_obstacle(self):
        """Method for returning a statement that a traffic light is detected."""

        return 'traffic light'

class Control_Database:
    """Control Databse class
    
    The key class for all interaction with the data. 
    It is responsible for the manipulation and handling of the data of the driverless car. 
    It is the super class of the Control Car Computer class.
    Positon: Time, speed, direction.
    
    Attribute:
        time (int): Time in hour (h).
        speed (int): Speed in km/h.
        distance (int): Distance in km.
        car: Information about the driverless car (Component class Driverless Car).
        obstacle_position_list (list): List of position data from all obstacles.
        driverless_car_position_list (list): List of the position data of the driverless car.
    """

    def __init__(self, time, speed, distance, car):
        """Inits Control Database class."""

        self.time = time
        self.speed = speed
        self.distance = distance
        self.car = car
        self.obstacle_position_list = []
        self.driverless_car_position_list = []

    def __repr__(self):
        """Represent class object as a string."""
        
        return f'Driverless_Car({self.time}h, {self.speed}km/h, {self.distance}km)'

    def add_obstacle_position(self, obstacle):
        """Method for adding position data of an obstacle to the obstacle list.

        Parameter: 
            obstacle: Obstacle object.
        
        Return:
            obstacle_position_list: List of all obstacles.
        """

        self.obstacle_position_list.append(obstacle)
        return self.obstacle_position_list

    def add_driverless_car_position(self, car_computer):
        """Method for adding position data of the driverless car to the driverless car list.

        Parameter: 
            car_computer: Control Car Computer object.
        
        Return:
            driverless_car_position_list: Postion data list of the driverless car.
        """

        self.driverless_car_position_list.append(car_computer)
        return self.driverless_car_position_list

    def show_obstacle_position(self):
        """Method for printing the obstacle position list."""

        print(self.obstacle_position_list)

    def show_driverless_car_position(self):
        """Method for printing the driverless position list."""

        print(self.driverless_car_position_list)

    def update_position_obstacle(self, obstacle):
        """Method for updating position data of a obstacle.
        
        Return: 
            obstacle_position_list: Return the obstacle position list.
        """

        for object in self.obstacle_position_list:
            if object == obstacle:
                self.obstacle_position_list.remove(object)
        return self.obstacle_position_list

    def update_position_driverless_car(self, car_data):
        """Method for updating position data of a obstacle.

        Parameter: 
            car_data: Control Car Computer object.
        
        Return: 
            obstacle_position_list: Return the obstacle position list.
        """
            
        for object in self.driverless_car_position_list:
            if object == car_data:
                self.driverless_car_position_list.remove(object)
        return self.driverless_car_position_list

class Control_Car_Computer(Control_Database):
    """Control Car Computer class
    
    The key of the driverless car. It controls all the action of the driverless car and 
    is the subclass of the database class.
    """

    def start(self, car):
        """Method for a driverless car action."""
        
        print(f'{car.model} is starting')

    def stop(self, car):
        """Method for a driverless car action."""

        print(f'{car.model} is stopping')

    def drive(self, car):
        """Method for a driverless car action."""

        print(f'{car.model} is moving forward')

    def brake(self, car):
        """Method for a driverless car action."""

        print(f'{car.model} is braking')

    def steer(self, car):
        """Method for a driverless car action."""

        print(f'{car.model} is steering')

    def obstacle_control(self, obstacle, new_obstacle):
        """Method for controlling the obstacle and for executing the
        method for updating the obstacle position.
        """

        if obstacle.id == new_obstacle.id:
            self.update_position_obstacle(obstacle)

    def traffic_light_control(self, traffic_light, car):
        """Method for handling the traffic lights.

        Return:
            move: Driverless car moves forward if the traffic light is green or 
            yellow (car is close enough to traffic light).

            brake: Driverless car brakes if the traffic light is red or 
            yellow (car is too far from traffic light).
        """

        if traffic_light.colour == 'green':
            self.drive(car)
            return 'move'
        elif traffic_light.colour == 'yellow':
            self.speed = self.speed / 3.6
            distance = (traffic_light.distance*1000) - (self.distance*1000)
            time = distance / self.speed
            if time > 2.5:
                print('Car is too far from traffic light')
                self.brake(car)
                return 'brake'
            else: 
                print('Car is close enough to traffic light')
                self.drive(car)
                return 'move'
        elif traffic_light.colour == 'red':
                self.brake(car)
                return 'brake'
        
class Camera:
    """Camera class
    
    A class for detecting obstacles or traffic lights by the driverless car's camera.
    """

    def detect_obstacle(self, obstacle):
        """Method for printing that the camera has detected an obstacle."""

        print(f'Camera has detected a {obstacle.detect_obstacle()}')

    def traffic_light_colour(self, colour):
        """Method for printing that the camera has detected colour of the traffic light.
        """

        print(f'Traffic light is {colour.get_traffic_light_colour()}')


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
    
    car = Driverless_Car('VW', 'ID.5')
    gps = GPS('Mainstreet 50670 Cologne')
    control_car = Control_Car_Computer(3.0, 50, 300, car)
    route = Route()
    camera = Camera()
    traffic_light = Traffic_light(3.0002, 0, 300.02, 'yellow')
    
    print('Traffic Light Scenario \n')
    print('Showing current position:')
    gps.driverless_car_position()

    print('\nCurrent status of the driverless car:')
    control_car.drive(car)

    print('\nNew information from the navigation system:')
    route.route_information(traffic_light)

    print('\nCamera is perceiving the environment:')
    camera.detect_obstacle(traffic_light)

    print('\nTraffic light colour:')
    camera.traffic_light_colour(traffic_light)

    print('\nPosition of traffic light and driverless car are saved in the database')
    control_car.add_driverless_car_position(control_car)
    control_car.add_obstacle_position(traffic_light)

    print('\nPosition shows when the traffic light is reached on the route.', end=' ')
    print('(Time in h, speed in km/h, distance in km)')
    print('Since the traffic lights are stationary, only the time and distance are relevant:')
    control_car.show_obstacle_position()

    print('\nCurrent position of the driverless car on the route.', end=' ')
    print('(Time in h, speed in km/h, distance in km):')
    control_car.show_driverless_car_position()

    print('\nCalculation if the driverless car has to brake or move forward', end=' ')
    print('based on the traffic light colour:')
    control_car.traffic_light_control(traffic_light, car)

if __name__ == '__main__':
    main()