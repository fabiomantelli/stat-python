import unittest
from utils.get_servers import get_server

class TestGetServer(unittest.TestCase):

    def test_get_server_if_parameter_name_is_invalid(self):
        name = "wrong_name"
        result = get_server(name)
        self.assertEqual(result, None)

    def test_get_server_if_parameter_name_is_not_a_string(self):
        name = {}
        result = get_server(name)
        self.assertEqual(result, None)
 
    def test_get_server_if_parameter_name_is_correct(self):
        name = "brazil"
        result = get_server(name)
        self.assertEqual(result, "150.162.19.214")

