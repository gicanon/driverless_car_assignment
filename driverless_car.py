import itertools

class Passenger:

    id_iter = itertools.count() # sequence counter (usually used for IDs)

    #alternative method:
    # count = 0

    # @classmethod
    # def incr(cls):
    #     cls.count += 1
    #     return cls.count

    def __init__(self):
        # self.user_ID = Passenger.incr()
        self.user_ID = next(Passenger.id_iter) + 1
        self.first_name = input('Enter your first name: ')
        self.last_name = input('Enter your last name: ')
        self.account_name = input('Enter an account name: ')
        self.password = input('Enter a password: ')
        self.email = input('Enter your email address: ')

    def __repr__(self):
        return f'User ({self.user_ID}) {self.account_name}'
       
class User(Passenger):

    def __init__(self, car):
        self.car = car
        self.users = []
        self.index = 0

    def display(self, car):
        while True:
            print(f'Welcome to {car.brand} {car.model}. \nPlease log into your account.')
            print('If you do not have an account please register a new account \n')
            choice = input('(L)og in \n(R)egister a new account \n(Q)uit \n> ').lower()
            if choice == 'l':
                result = self.login()
                if result == 'start':
                    return 'start'
            elif choice == 'r':
                print()
                self.register()
            elif choice == 'q':
                return 'quit'
            else:
                print('Please enter the corresponding input for the function \n')

    def __add__(self, new_user):
        user_list = []
        user_list.append(new_user)
        self.users.append(user_list)

    def register(self):
        self + Passenger()
        print('You have successfully registered \n')
        print('Registered users:')
        print(self.users, '\n')

    def login(self):
        if len(self.users) == 0:
            print('Please register at least one user account \n')
            return 'empty'
        else:
            print('Please login with your account name and password \n')
            user_list = self.verify_account()
            if user_list == 'quit':
                return 'fail'
            else:
                check_login = self.verify_password(user_list)
                if check_login == True:
                    result = self.after_login(user_list)
                    if result == 'start':
                        return 'start'
                    else: 
                        return 'logout'
                else: 
                    return 'fail'

    def verify_account(self):
        user_list = []
        account_name = input('Enter your account name: ').lower()
        for user in self.users:
            user_list = user
            for name in user_list:
                if name.account_name == account_name:
                    print('Account name is correct \n')
                    return user_list
        print('Account name is not correct, please try again or quit \n')
        choice = input('(N)ext try \n(Q)uit \n> ').lower()  
        if choice == 'q':
            print()
            return 'quit'
        elif choice == 'n':
            print()
            return self.verify_account()
        else: 
            print('Wrong input, try again! \n')
            return self.verify_account()

    def verify_password(self, user_list):
        password = input('Enter your password: ').lower()
        for pw in user_list:
            if pw.password == password:
                print('Password  is correct \n')
                for name in user_list:
                    print(f'Hello {name.first_name} {name.last_name}, your login was successful \n')
                return True
        print('Password is not correct, please try again or quit \n ')  
        choice = input('(N)ext try \n(Q)uit \n> ').lower()  
        if choice == 'q':
            print()   
            return 'fail'
        elif choice == 'n':
            print()
            return self.verify_password(user_list)
        else: 
            print('Wrong input, try again! \n')
            return self.verify_password(user_list)

    def after_login(self, user_list):
        self.show_user_account(user_list)
        choice = input('\n(S)tarting Travel \n(U)pdate Profil \n(D)elete account \n(L)ogout \n> ').lower()
        if choice == 's':
            print('Starting navigation system')
            return 'start'
        elif choice == 'u':
            print()
            self.update_profile(user_list)
            self.show_all_user_data(user_list)
            return self.after_login(user_list)
        elif choice == 'l':
            print('Logout was successful ')
            print()
            return 'logout'
        elif choice == 'd':
            print()
            self.delete_account(user_list)
            return 'delete'
        else:
            print('Wrong input, try again! \n')
            return self.after_login(user_list)

    def show_user_account(self, user_list):
        for index, info in enumerate(user_list):
            index = info.user_ID
            print(f'User ID: {index} Account name: {info.account_name}')

    def show_all_user_data(self, user_list):
         for index, info in enumerate(user_list):
            index = info.user_ID
            print(f'User ID: {index} \nFirst name: {info.first_name}')
            print(f'Last name: {info.last_name} \nAccount name: {info.account_name}')
            print(f'Password: *** \nEmail address: {info.email}\n')

    def update_profile(self, user_list):
        print('Enter the corresponding number for editing information:')
        print('(1) First name \n(2) Last name \n(3) Account name \n(4) Password \n(5) Email address')
        choice = input('> ')
        for user in self.users:
            index = self.users.index(user)
            if user == user_list:
                self.users.remove(user)
        for name in user_list:
            if choice == '1':
                name.first_name = input('\nEnter new first name: ')
            elif choice == '2':
                name.last_name = input('\nEnter new last name: ')
            elif choice == '3':
                name.account_name = input('\nEnter new account name: ')
            elif choice == '4':
                name.password = input('\nEnter new password: ')
            elif choice == '5':
                name.email = input('\nEnter new email address: ')
            else:
                print('Wrong input, try again! \n')
                return self.update_profile(user_list)
        self.users.insert(index, user_list)
        print('Editing was successful \n')
        return 'update'

    def delete_account(self, user_list):
        print('Do you want to delete your account? \n')
        choice = input('(D)elete \n(Q)uit \n> ').lower()
        if choice == 'd':
            for user in self.users:
                if user == user_list:
                    self.users.remove(user)
                    print('Deleting account was successful \n')
                    print('Registered users:')
                    print(self.users, '\n')
        elif choice == 'q':
            return self.after_login(user_list)
        else:
            print('Wrong input, try again! \n')
            return self.delete_account(user_list)

class Driverless_Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

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

