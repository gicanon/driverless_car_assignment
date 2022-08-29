"""Test route planning file

Unit test for the second driverless car scenario. Route planning.

Import Unittest module:
    An automatic test runner module for testing code.
Import the Route and Navigation classes from the route_planning.py file:
    The code that needs to be tested
"""

import unittest 
from route_planning import Route, Navigation

class TestUsing_unitest(unittest.TestCase):
    """Test class

    class is a subclass of TestCase from the module unittest.
    An automatic test runner module for testing code.
    The test methods are tested with the help of assertion.
    """
    
    def test_add_destination(self):
        """Test if the destination list is not 0 after adding
        a destination."""

        result = len(navi.add_destination())
        self.assertIsNot(result, 0)

    def test_search_destination(self):
        """Test if the added destination is 'Rom'."""

        print('\nEnter the destination: rom\n')
        result = navi.search_destination()
        self.assertEqual(result, 'Rom')

    def test_update_destination(self):
        """Test if the updated destination is 'Berlin'."""

        print('\nEnter the destination: berlin\n')
        result = navi.update_destination()
        self.assertEqual(result, 'Berlin')

    def test_x_delete_destination(self):
        """Test if the destination list is 0 after deleting the destination."""

        result = len(navi.delete_destination())
        self.assertEqual(result, 0)

    def test_calculate_route(self):
        """Test if the route was succesful calculated."""

        result = route.calculate_route(navi)
        self.assertTrue(result, True)

    def test_start_navigation_accept(self):
        """Test if the navigation has been started."""

        print('\nAccept the route \n')
        result = route.start_navigation(navi)
        self.assertEqual(result, 'start')

    def test_start_navigation_cancel(self):
        """Test if the route operation was cancelled."""

        print('\nCancel the route \n')
        result = route.start_navigation(navi)
        self.assertEqual(result, 'cancel')

route = Route()
navi = Navigation('Wolfsburg', route)


if __name__ == '__main__':
    unittest.main()