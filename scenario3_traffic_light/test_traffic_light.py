"""Test traffic light

Unit test for the third driverless car scenario. Dealing with the traffic light.

Import Unittest module:
    An automatic test runner module for testing code.
Import the Driverless_Car, GPS, Control_Car_Computer, Route, Camera and Traffic_light
classes from the traffic_light.py file:
    The code that needs to be tested
"""

import unittest 
from traffic_light import Driverless_Car, GPS, Control_Car_Computer, \
    Route, Camera, Traffic_light


class TestUsing_unitest(unittest.TestCase):
    """Test class
    
    class is a subclass of TestCase from the module unittest.
    An automatic test runner module for testing code.
    The test methods are tested with the help of assertion.
    """

    def test_get_traffic_light_colour(self):
        """Test if the traffic light is yellow."""

        result = traffic_light.get_traffic_light_colour()
        self.assertIs(result, 'yellow')

    def test_detect_obstacle(self):
        """Test if a traffic light is detected."""

        result = traffic_light.detect_obstacle()
        self.assertEqual(result, 'traffic light')
    
    def test_add_obstacle_position(self):
        """Test if the obstacle position list is not 0."""

        result = len(control_car.add_obstacle_position(traffic_light))
        self.assertIsNot(result, 0)

    def test_add_driverless_car_position(self):
        """Test if the driverless car position list is not 0."""

        result = len(control_car.add_driverless_car_position(control_car))
        self.assertIsNot(result, 0)

    def test_traffic_light_control(self):
        """Test if the car moves forward after detecting 
        the traffic light's colour and calculating the driverless car's
        and the traffic light position.
        """

        result = control_car.traffic_light_control(traffic_light, car)
        self.assertEqual(result, 'move')

car = Driverless_Car('VW', 'ID.5')
gps = GPS('Mainstreet 50670 Cologne')
control_car = Control_Car_Computer(3.0, 50, 300, car)
route = Route()
camera = Camera()
traffic_light = Traffic_light(3.0002, 0, 300.02, 'yellow')

if __name__ == '__main__':
    unittest.main()