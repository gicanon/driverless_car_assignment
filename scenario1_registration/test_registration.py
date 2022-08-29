import unittest
from registration import Driverless_Car, User


class TestUsing_unitest(unittest.TestCase):
    
    def test1_login_empty(self):
        print('\nLog in without registering an account \n')
        result = u1.login()
        self.assertEqual(result, 'empty')

    def test2_display_quit(self):
        print('\nQuit the display \n')
        result = u1.display(car)
        self.assertEqual(result, 'quit')

    def test3_display_start(self):
        print('\nStart the travel \n')
        result = u1.display(car)
        self.assertEqual(result, 'start')
    
    def test4_login_fail(self):
        print('\nFail to log in \n')
        result = u1.login()
        self.assertEqual(result, 'fail')

    def test5_login_logout(self):
        print('\nLOG OUT OF YOUR ACCOUNT (Log in with your previously registered account) \n')
        result = u1.login()
        self.assertEqual(result, 'logout')

    def test6_verify_account(self):
        print('\nEnter your registered user account \n')
        result = len(u1.verify_account())
        self.assertIsNot(result, 0)

    def test7_verify_password(self):
        print('\nLog in with your password\n')
        result = u1.verify_password(u1.verify_account())
        self.assertEqual(result, True)

    def test8_update_profile(self):
        print('\nUpdate your profile \n')
        result = u1.update_profile(u1.verify_account())
        self.assertEqual(result, 'update')

    def test9_after_login_delete(self):
        print('\nDelete your account \n')
        result = u1.after_login(u1.verify_account())
        self.assertEqual(result, 'delete')


car = Driverless_Car('Volskwagen', 'ID.5')
u1 = User(car)
user_list = []

if __name__ == '__main__':
    unittest.main()