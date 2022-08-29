class Obstacle:
    
    def __init__(self, time, speed, distance, id = None):
        self.time = time
        self.speed = speed
        self.distance = distance
        self.id = id

class Pedestrian(Obstacle):

    def detect_obstacle(self):
        return 'pedestrian'

    def __repr__(self):
        return f'Pedestrian({self.time}h, {self.speed}km/h, {self.distance}km)' 

class Vehicle(Obstacle):

    def detect_obstacle(self):
        return 'vehicle'

    def __repr__(self):
        return f'Vehicle({self.time}h, {self.speed}km/h, {self.distance}km)' 

class Unknown(Obstacle):

    def detect_obstacle(self):
        return 'obstacle (unknown)'

    def __repr__(self):
        return f'Unknown({self.time}h, {self.speed}km/h, {self.distance}km)'

class Control_Database:

    def __init__(self, time, speed, distance, car):
        self.time = time
        self.distance = distance
        self.car = car
        self.speed = speed
        self.obstacle_position_list = []
        self.driverless_car_position_list = []

    def __repr__(self):
        return f'Driverless_Car({self.time}h, {self.speed}km/h, {self.distance}km)'

    def add_obstacle_position(self, obstacle):
        self.obstacle_position_list.append(obstacle)
        return self.obstacle_position_list

    def add_driverless_car_position(self, car_computer):
        self.driverless_car_position_list.append(car_computer)
        return self.driverless_car_position_list

    def show_obstacle_position(self):
        print(self.obstacle_position_list)

    def show_driverless_car_position(self):
        print(self.driverless_car_position_list)

    def update_position_obstacle(self, obstacle):
        for object in self.obstacle_position_list:
            if object == obstacle:
                self.obstacle_position_list.remove(object)
        return self.obstacle_position_list

    def update_position_driverless_car(self, car_data):
        for object in self.driverless_car_position_list:
            if object == car_data:
                self.driverless_car_position_list.remove(object)
        return self.driverless_car_position_list

class Control_Car_Computer(Control_Database):

    def start(self, car):
        print(f'{car.model} is starting')

    def stop(self, car):
        print(f'{car.model} is stopping')

    def drive(self, car):
        print(f'{car.model} is moving forward')

    def brake(self, car):
        print(f'{car.model} is braking')

    def steer(self, car):
        print(f'{car.model} is steering')

    def obstacle_control(self, obstacle, new_obstacle):
        if obstacle.id == new_obstacle.id:
            self.update_position_obstacle(obstacle)

    def traffic_light_control(self, traffic_light, car):
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

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class GPS:
    def __init__(self, current_position):
        self.current_position = current_position

    def driverless_car_position(self):
        print(f'Your current position is {self.current_position}')
        
class Camera:

    def detect_obstacle(self, obstacle):
        print(f'Camera has detected a(n) {obstacle.detect_obstacle()}')

    def traffic_light_colour(self, colour):
        print(f'Traffic light is {colour.get_traffic_light_colour()}')

class Sensor:

     def detect_obstacle(self, obstacle):
        print(f'Sensor has detected a(n) {obstacle.detect_obstacle()}')

class Ultrasonic_Sensor(Sensor):

     def detect_obstacle(self, obstacle):
        print(f'Ultrasonic Sensor has detected a(n) {obstacle.detect_obstacle()}')

class Radar_Sensor(Sensor):

     def detect_obstacle(self, obstacle):
        print(f'Radar Sensor has detected a(n) {obstacle.detect_obstacle()}')

class Lidar(Sensor):

     def detect_obstacle(self, obstacle):
        print(f'Lidar Sensor has detected a(n) {obstacle.detect_obstacle()}')

def main():

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



