"""Test registration file

Unit test for the first driverless car scenario. Registration of an account.

Import Unittest module:
    An automatic test runner module for testing code.
Import the Driverless_Car and User classes from the registration.py file:
    The code that needs to be tested
"""

import unittest
from registration import Driverless_Car, User


class TestUsing_unitest(unittest.TestCase):
    """Test class
    
    class is a subclass of TestCase from the module unittest.
    An automatic test runner module for testing code.
    The test methods are tested with the help of assertion.
    """
    
    def test1_login_empty(self):
        """Test 1: Test if the user list is empty by
        attempting to log in without registering an account."""

        print('\nLog in without registering an account \n')
        result = u1.login()
        self.assertEqual(result, 'empty')

    def test2_display_quit(self):
        """Test 2: Test if the process is terminated."""

        print('\nQuit the login and registration process \n')
        result = u1.display(car)
        self.assertEqual(result, 'quit')

    def test3_display_start(self):
        """Test 3: Test if the user can start the travel."""

        print('\nStart the travel \n')
        result = u1.display(car)
        self.assertEqual(result, 'start')
    
    def test4_login_fail(self):
        """Test 4: Test if user can fail to log in."""

        print('\nFail to log in \n')
        result = u1.login()
        self.assertEqual(result, 'fail')

    def test5_login_logout(self):
        """Test 5: Test if user can log out of their account."""

        print('\nLog out of your acount (Log in with your previously registered account) \n')
        result = u1.login()
        self.assertEqual(result, 'logout')

    def test6_verify_account(self):
        """Test 6: Test if a user list is returned after checking the account name."""

        print('\nEnter your registered user account name \n')
        result = len(u1.verify_account())
        self.assertIsNot(result, 0)

    def test7_verify_password(self):
        """Test 7: Test if the password is true."""

        print('\nLog in with your password\n')
        result = u1.verify_password(u1.verify_account())
        self.assertEqual(result, True)

    def test8_update_profile(self):
        """Test 8: Test if the account has been updated."""

        print('\nUpdate your profile \n')
        result = u1.update_profile(u1.verify_account())
        self.assertEqual(result, 'update')

    def test9_after_login_delete(self):
        """Test 9: Test if the account has been deleted."""

        print('\nDelete your account \n')
        result = u1.after_login(u1.verify_account())
        self.assertEqual(result, 'delete')


car = Driverless_Car('Volskwagen', 'ID.5')
u1 = User(car)
user_list = []

if __name__ == '__main__':
    unittest.main()