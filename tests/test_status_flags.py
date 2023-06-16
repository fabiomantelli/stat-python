import unittest
from app.utils.status_flags_handler import status_flags

class TestGoodStatusFlags(unittest.TestCase):
    
    def test_status_flags_if_data_error(self):
        data = 557056
        result = status_flags(data)
        self.assertEqual(result, True)
        
    def test_status_flags_if_data_quality_sync(self):
        data = 64
        result = status_flags(data)
        self.assertEqual(result, True)

    def test_status_flags_if_data_ok(self):
        data = 0
        result = status_flags(data)
        self.assertEqual(result, True)        

    def test_status_flags_if_pmu_error(self):
        data = 909312
        result = status_flags(data)
        self.assertEqual(result, True)

    def test_status_flags_if_data_dif(self):
        data = 909808
        result = status_flags(data)
        self.assertEqual(result, False)
