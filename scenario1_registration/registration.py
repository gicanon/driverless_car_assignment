"""Registration file

This file is created to register an account for the use of a driverless car. 
It has a text-based user interface where the user is prompted 
to make the appropriate entries. After running the file, 
the user must continue driving by registering an account or exiting the programme.

Import module itertools:
    It is used to count the sequence. 
    In this case, it counts the user IDs for each registration.
"""

import itertools

class Passenger:
    """Passenger class:

    It is built to create the profile of an account.
    It does not have parameters as the user has to enter their personal information.

    Class variable id_iter: 
        It is assigned to the method itertools.count() for counting the created IDs.

    Attributes: 
        user_ID (int): Unique user ID for each registered account.
        first_name (str): First name of the passenger.
        last_name (str): Last name of the passenger.
        account_name (str): Account name of the passenger.
        password (str): Password of the passenger.
        email (str): Email address of the passenger.

    The attributes are all public.
    """

    id_iter = itertools.count() # sequence counter (usually used for IDs)

    #alternative method:

    # count = 0

    # @classmethod
    # def incr(cls):
    #     cls.count += 1
    #     return cls.count

    def __init__(self):
        """Inits object of the Passenger class."""

        # self.user_ID = Passenger.incr()
        self.user_ID = next(Passenger.id_iter) + 1
        self.first_name = input('Enter your first name: ')
        self.last_name = input('Enter your last name: ')
        self.account_name = input('Enter an account name: ')
        self.password = input('Enter a password: ')
        self.email = input('Enter your email address: ')

    def __repr__(self):
        """Represent class object as a string."""

        return f'User ({self.user_ID}) {self.account_name}'
       
class User(Passenger):
    """ User class:
    
    The subclass of Passenger class for creating a user account.
    It has a text-based user interface where the user is prompted 
    to make the appropriate entries.
    After running the file, the user must continue driving 
    by registering an account or exiting the programme.
    
    Attributes:
        car: Information about the driverless car (Component class Driverless Car).
        users (list): List where all user accounts are stored.
        index (int): Assigned index to 0.
    """

    def __init__(self, car):
        """Inits User class."""

        self.car = car
        self.users = []
        self.index = 0

    def display(self, car):
        """The key to the registration process. After running the function, 
        it can only be interrupted if the user quits or starts the travel.
        
        Parameters:
            car: Information about the driverless car (Component class Driverless Car).

        Return:
            start: Start the travel.
            quit: Quit the program.
        """

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
        """Built-in method for manipulating the addition operator.
        
        Parameter:
            new_user: Add a new Passenger obeject to the list.
        """

        user_list = []
        user_list.append(new_user)
        self.users.append(user_list)

    def register(self):
        """The method is responsible for registering an account and 
        saving it in the user list.
        """

        self + Passenger()  # Used the built-in function __add__
        print('You have successfully registered \n')
        print('Registered users:')
        print(self.users, '\n')

    def login(self):
        """Method to log in with the registered user account.
        
        Return: 
            empty: List is empty.
            fail: Login failed.
            start: Start the travel.
            logout: Logout of the account.
        """

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
        """Method to verify the account name.
        
        Return: 
            user_list: Account name was correct and the user list is returned.
            quit: Quit the verify process.
            Method verify_account: Next try to enter the account name.
            """

        user_list = []
        account_name = input('Enter your account name: ').lower()
        for user in self.users:
            user_list = user
            for name in user_list:
                if name.account_name == account_name:
                    print('Account name is correct \n')
                    return user_list    
        print('Account name is not correct, please try again or quit \n')   # It only occurs if the account is incorrect.
        choice = input('(N)ext try \n(Q)uit \n> ').lower()  
        if choice == 'q':
            print()
            return 'quit'   # By quitting the entry the display function will occur
        elif choice == 'n':
            print()
            return self.verify_account()
        else: 
            print('Wrong input, try again! \n')
            return self.verify_account()

    def verify_password(self, user_list):
        """Method to verify the password
        
        Parameter:
            user_list: list with the data of the user account.
            
        Return:
            True: Password is correct and login was successful.
            fail: Password is not correct and user quit the process.
            Method verify_password(): Next try to enter the password.
        """

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
        """Method where the user can choose whether to start the journey, 
        update the profile, delete the account or log out of the account.
        
        Parameter:
            user_list: List with the data of the user account.
            
        Return:
            start: Start the travel.
            logout: Logout from the account.
            delete: Delete the user account.
            Method after_login: Execute the method again if an incorrect entry was made.
        """

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
        """Method for printing the user ID and account name as a string.
        
        Parameter:
            user_list: List with the data of the user account.
        """

        for index, info in enumerate(user_list):
            index = info.user_ID
            print(f'User ID: {index} Account name: {info.account_name}')

    def show_all_user_data(self, user_list):
        """Method for printing all user data among each other as a string.
        
        Parameter:
            user_list: List with the data of the user account.
        """

        for index, info in enumerate(user_list):
            index = info.user_ID
            print(f'User ID: {index} \nFirst name: {info.first_name}')
            print(f'Last name: {info.last_name} \nAccount name: {info.account_name}')
            print(f'Password: *** \nEmail address: {info.email}\n')

    def update_profile(self, user_list):
        """Method for updating the user account after selection by the user.
        
        Parameter:
            user_list: List with the data of the user account.

        Return: 
            Method update_profile: Execute the method again if an incorrect entry was made.
            update: Account has been updated.

        """

        print('Enter the corresponding number for editing information:')
        print('(1) First name \n(2) Last name \n(3) Account name \n(4) Password \n(5) Email address')
        choice = input('> ')
        for user in self.users:
            index = self.users.index(user)
            if user == user_list:
                self.users.remove(user)     # The previous user account is deleted.
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
        self.users.insert(index, user_list)     # The new user account is added to the user list.
        print('Editing was successful \n')
        return 'update'

    def delete_account(self, user_list):
        """Method for deleting the user account and logging out of the account.
        
        Parameter:
            user_list: List with the data of the user account.
        
        Return:
            Method after_login: User exits the deletion process and the after_login
            is executed.
            Method delete_account: Execute the method again if an incorrect entry was made. 
        """
        
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
            
def main():
    """Main function to create the objects and execute the file."""

    car = Driverless_Car('Volskwagen', 'ID.5')
    u1 = User(car)

    u1.display(car)

if __name__ == '__main__':
    main()
