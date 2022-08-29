class Driverless_Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Obstacle:
    
   def __init__(self, time, speed, distance, id = None):
        self.time = time
        self.speed = speed
        self.distance = distance
        self.id = id

class Traffic_light(Obstacle):

    def __init__(self, time, speed, distance, colour):
        super().__init__(time, speed, distance)
        self.colour = colour

    def __repr__(self):
        return f'Traffic_Light({self.time}h, {self.speed}km/h, {self.distance}km)' 

    def route_info(self):
        print('Traffic light is incoming')

    def get_traffic_light_colour(self):
        return self.colour

    def detect_obstacle(self):
        return 'traffic light'

class Control_Database:

    def __init__(self, time, speed, distance, car):
        self.time = time
        self.speed = speed
        self.distance = distance
        self.car = car
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
        
class Camera:

    def detect_obstacle(self, obstacle):
        print(f'Camera has detected a {obstacle.detect_obstacle()}')

    def traffic_light_colour(self, colour):
        print(f'Traffic light is {colour.get_traffic_light_colour()}')

class GPS:
    def __init__(self, current_position):
        self.current_position = current_position

    def driverless_car_position(self):
        print(f'Your current position is {self.current_position}')


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