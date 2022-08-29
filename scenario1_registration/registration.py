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
            
def main():

    car = Driverless_Car('Volskwagen', 'ID.5')
    u1 = User(car)

    u1.display(car)

if __name__ == '__main__':
    main()
