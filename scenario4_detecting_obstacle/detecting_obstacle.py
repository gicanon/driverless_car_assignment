"""Detecting obstacle file

A file for demonstrating an obstacle detection scenario.
"""

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

class Pedestrian(Obstacle):
    """Pedestrian class

    A subclass of obstacles that represent a pedestrian."""

    def detect_obstacle(self):
        """Method for returning a statement that a pedestrian is detected."""

        return 'pedestrian'

    def __repr__(self):
        """Represent class object as a string."""

        return f'Pedestrian({self.time}h, {self.speed}km/h, {self.distance}km)' 

class Vehicle(Obstacle):
    """Vehicle class

    A subclass of obstacles that represent a pedestrian."""

    def detect_obstacle(self):
        """Method for returning a statement that a vehicle is detected."""

        return 'vehicle'

    def __repr__(self):
        """Represent class object as a string."""

        return f'Vehicle({self.time}h, {self.speed}km/h, {self.distance}km)' 

class Unknown(Obstacle):

    def detect_obstacle(self):
        """Method for returning a statement that a unkown (obstacle) is detected."""

        return 'obstacle (unknown)'

    def __repr__(self):
        """Represent class object as a string."""

        return f'Unknown({self.time}h, {self.speed}km/h, {self.distance}km)'

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
        
class Camera:
    """Camera class
    
    A class for detecting obstacles or traffic lights by the driverless car's camera.
    """

    def detect_obstacle(self, obstacle):
        """Method for printing that the camera has detected an obstacle."""

        print(f'Camera has detected a {obstacle.detect_obstacle()}')

    def traffic_light_colour(self, colour):
        """Method for printing that the camera has detected colour of the traffic light."""

        print(f'Traffic light is {colour.get_traffic_light_colour()}')

class Sensor:
    """Sensor class
    
    A super class for all driverless car sensors to detect obstacles."""

    def detect_obstacle(self, obstacle):
        """Method for printing that a sensor has detected an obstacle."""

        print(f'Sensor has detected a(n) {obstacle.detect_obstacle()}')

class Ultrasonic_Sensor(Sensor):
    """Ultrasonic Sensor class
    
    A subclass of Sensor class for detecting obstacles by the driverless car's Ultrasonic sensor."""

    def detect_obstacle(self, obstacle):
        """Method for printing that the Ultrasonic sensor has detected an obstacle."""

        print(f'Ultrasonic Sensor has detected a(n) {obstacle.detect_obstacle()}')

class Radar_Sensor(Sensor):
    """Radar Sensor class
    
    A subclass of Sensor class for detecting obstacles by the driverless car's Radar sensor."""

    def detect_obstacle(self, obstacle):
        """Method for printing that the Radar sensor has detected an obstacle."""

        print(f'Radar Sensor has detected a(n) {obstacle.detect_obstacle()}')

class Lidar(Sensor):
    """Lidar Sensor class
    
    A subclass of Sensor class for detecting obstacles by the driverless car's Lidar sensor."""

    def detect_obstacle(self, obstacle):
        """Method for printing that the Lidar sensor has detected an obstacle."""

        print(f'Lidar Sensor has detected a(n) {obstacle.detect_obstacle()}')

def main():
    """Main function to create the objects and execute the file."""

    car = Driverless_Car('VW', 'ID.5')
    gps = GPS('Wolfsburg')
    control_car = Control_Car_Computer(5.0, 80, 500, car)
    camera = Camera()
    lidar = Lidar()
    radar = Radar_Sensor()

    pedestrian = Pedestrian(5.0002, 3.6, 500.01, 1)
    vehicle = Vehicle(5.0002, 50, 500.02, 1)
    vehicle_2 = Vehicle(5.0002, 100, 500.02, 1)
    unknown = Unknown(5.0003, 10, 501, 1)

    print('Detecting Obstacle Scenario\n')
    print('Showing current position:')
    gps.driverless_car_position()
    
    print('\nCamera is perceiving the environment:')
    camera.detect_obstacle(pedestrian)
    camera.detect_obstacle(vehicle)

    print('\nLidar Sensor is perceiving the environment:')
    lidar.detect_obstacle(vehicle_2)

    print('\nRadar is perceiving the environment:')
    radar.detect_obstacle(unknown)

    print('\nObstacles are saved in the database')
    control_car.add_obstacle_position(pedestrian)
    control_car.add_obstacle_position(vehicle)
    control_car.add_obstacle_position(vehicle_2)
    control_car.add_obstacle_position(unknown)

    print('\nShowing list of obstacles:')
    control_car.show_obstacle_position()

    print('\nDoes new detected obstacle match saved obstacle?')
    print('Yes, update obstacle list and remove previous obstacle')
    control_car.obstacle_control(vehicle, vehicle_2)
    
    print('\nShowing new list of obstacles:')
    control_car.show_obstacle_position()

if __name__ == '__main__':
    main()



