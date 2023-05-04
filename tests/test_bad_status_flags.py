import unittest
from utils.good_status_flags import good_status_flags

class TestProcessData(unittest.TestCase):
    
    def test_good_status_flags_if_data_error(self):
        data = 557056
        result = good_status_flags(data)
        self.assertEqual(result, True)
        
    def test_good_status_flags_if_data_quality_sync(self):
        data = 64
        result = good_status_flags(data)
        self.assertEqual(result, True)

    def test_good_status_flags_if_data_ok(self):
        data = 0
        result = good_status_flags(data)
        self.assertEqual(result, True)
