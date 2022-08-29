import unittest 
from route_planning import Route, Navigation

class TestUsing_unitest(unittest.TestCase):
    
    def test_add_destination(self):
        result = len(navi.add_destination())
        self.assertIsNot(result, 0)

    def test_search_destination(self):
        print('\nEnter the destination: rom\n')
        result = navi.search_destination()
        self.assertEqual(result, 'Rom')

    def test_update_destination(self):
        print('\nEnter the destination: berlin\n')
        result = navi.update_destination()
        self.assertEqual(result, 'Berlin')

    def test_x_delete_destination(self):
        result = len(navi.delete_destination())
        self.assertEqual(result, 0)

    def test_calculate_route(self):
        result = route.calculate_route(navi)
        self.assertTrue(result, True)

    def test_start_navigation_accept(self):
        print('\nAccept the route \n')
        result = route.start_navigation(navi)
        self.assertEqual(result, 'start')

    def test_start_navigation_cancel(self):
        print('\nCancel the route \n')
        result = route.start_navigation(navi)
        self.assertEqual(result, 'cancel')

route = Route()
navi = Navigation('Wolfsburg', route)


if __name__ == '__main__':
    unittest.main()