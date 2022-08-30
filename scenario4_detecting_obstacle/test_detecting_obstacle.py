"""Test detecting obstacle file

Unit test for the fourth driverless car scenario. Detecting Obstacle.

Import Unittest module:
    An automatic test runner module for testing code.
Import the Driverless_Car, Control_Car_Computer, Unknown, Vehicle, Pedestrian
classes from the detecting_obstacle.py file:
    The code that needs to be tested.
"""

import unittest 
from detecting_obstacle import Driverless_Car, Control_Car_Computer, \
  Unknown, Vehicle, Pedestrian

class TestUsing_unitest(unittest.TestCase):
    """Test class
    
    class is a subclass of TestCase from the module unittest.
    An automatic test runner module for testing code.
    The test methods are tested with the help of assertion.
    """

    def test_detect_pedestrian(self):
        """Test if pedestrian is detected."""

        result = pedestrian.detect_obstacle()
        self.assertEqual(result, 'pedestrian')

    def test_detect_vehicle(self):
        """Test if vehicle is detected."""

        result = vehicle.detect_obstacle()
        self.assertEqual(result, 'vehicle')

    def test_detect_unknown(self):
        """Test if obstacle (unknown) is detected."""

        result = unknown.detect_obstacle()
        self.assertEqual(result, 'obstacle (unknown)')

    def test_add_obstacle_position(self):
        """Test if obstacle position list is not 0 after adding
        obstacle data to the list."""

        result = len(control_car.add_obstacle_position(pedestrian))
        self.assertIsNot(result, 0)

    def test_add_driverless_car_position(self):
        """Test if driverless car position list is not 0 after adding 
        driverless car data to the list."""

        result = len(control_car.add_driverless_car_position(control_car))
        self.assertIsNot(result, 0)

    def test_update_position_obstacle(self):
        """Test if obstacle position list is empty after updating the obstacle."""
        
        result = control_car.update_position_obstacle(pedestrian)
        self.assertEqual(result, [])

    def test_update_position_driverless_car(self):
        """Test if driverless position list is empty after updating the driverless car."""

        result = control_car.update_position_driverless_car(control_car)
        self.assertEqual(result, [])

car = Driverless_Car('VW', 'ID.5')
control_car = Control_Car_Computer(5.0, 80, 500, car)

pedestrian = Pedestrian(5.0002, 3.6, 500.01, 1)
vehicle = Vehicle(5.0002, 50, 500.02, 1)
vehicle_2 = Vehicle(5.0002, 100, 500.02, 1)
unknown = Unknown(5.0003, 10, 501, 1)

if __name__ == '__main__':
    unittest.main()