import unittest 
from detecting_obstacle import Driverless_Car, Control_Car_Computer, \
  Unknown, Vehicle, Pedestrian

class TestUsing_unitest(unittest.TestCase):

    def test_detect_pedestrian(self):
        result = pedestrian.detect_obstacle()
        self.assertEqual(result, 'pedestrian')

    def test_detect_vehicle(self):
        result = vehicle.detect_obstacle()
        self.assertEqual(result, 'vehicle')

    def test_detect_unknown(self):
        result = unknown.detect_obstacle()
        self.assertEqual(result, 'obstacle (unknown)')

    def test_add_obstacle_position(self):
        result = len(control_car.add_obstacle_position(pedestrian))
        self.assertIsNot(result, 0)

    def test_add_driverless_car_position(self):
        result = len(control_car.add_driverless_car_position(control_car))
        self.assertIsNot(result, 0)

    def test_update_position_obstacle(self):
        result = control_car.update_position_obstacle(pedestrian)
        self.assertEqual(result, [])

    def test_update_position_driverless_car(self):
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