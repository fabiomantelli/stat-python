import unittest
from app.utils.set_datetime import set_datetime

class TestSetDate(unittest.TestCase):
    
    def test_set_datetime_if_date_is_valid(self):
        date = "01-05-20"
        time = "00:00:00.000"
        result = set_datetime(date, time)
        self.assertEqual(result, "01-05-20 00:00:00.000")

    def test_set_datetime_is_invalid(self):
        date = "15-06-23"
        time = "00:00:00.000"
        result = set_datetime(date, time)
        self.assertEqual(result, "15-06-23 is not a valid date.")