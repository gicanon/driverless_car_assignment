import unittest 
from traffic_light import Driverless_Car, GPS, Control_Car_Computer, \
    Route, Camera, Traffic_light


class TestUsing_unitest(unittest.TestCase):

    def test_get_traffic_light_colour(self):
        result = traffic_light.get_traffic_light_colour()
        self.assertIs(result, 'yellow')

    def test_detect_obstacle(self):
        result = traffic_light.detect_obstacle()
        self.assertEqual(result, 'traffic light')
    
    def test_add_obstacle_position(self):
        result = len(control_car.add_obstacle_position(traffic_light))
        self.assertIsNot(result, 0)

    def test_add_driverless_car_position(self):
        result = len(control_car.add_driverless_car_position(control_car))
        self.assertIsNot(result, 0)

    def test_traffic_light_control(self):
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