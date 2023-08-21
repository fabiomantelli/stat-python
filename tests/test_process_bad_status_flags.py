import unittest
from app.process_bad_status_flags import StatusFlags

class TestProcessData(unittest.TestCase):
    def setUp(self):
        self.status_flags = StatusFlags()
    
    def test_process_bad_status_flags_with_empty_dict(self):
        data = {
            "TimeSeriesDataPoints": []
        }
        result = self.status_flags.process_bad_status_flags(data)
        self.assertEqual(result, [])
    
    def test_process_bad_status_flags_with_no_bad_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 0, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 557056, 'Quality': 29 },
            ]
        }
        result = self.status_flags.process_bad_status_flags(data)
        self.assertEqual(result, [])
    
    def test_process_bad_status_flags_with_single_first_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 64, 'Quality': 29 },
            ]
        }
        result = self.status_flags.process_bad_status_flags(data)

        expected = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
        ]
        self.assertEqual(result, expected)
    
    def test_process_bad_status_flags_with_single_last_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            ]
        }
        result = self.status_flags.process_bad_status_flags(data)

        expected = [
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
        ]
        self.assertEqual(result, expected)
    
    def test_process_bad_status_flags_with_single_first_and_single_last_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            ]
        }
        result = self.status_flags.process_bad_status_flags(data)

        expected = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
        ]
        self.assertEqual(result, expected)
    
    def test_process_bad_status_flags_with_two_firsts_and_single_last_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
            ]
        }
        result = self.status_flags.process_bad_status_flags(data)

        expected = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
        ]
        self.assertEqual(result, expected)
    
    def test_process_bad_status_flags_with_first_and_two_lasts_point_with_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
            ]
        }
        result = self.status_flags.process_bad_status_flags(data)

        expected = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
        ]
        self.assertEqual(result, expected)
    
    def test_process_bad_status_flags_with_first_and_second_diferent_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 88, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 64, 'Quality': 29 },
            ]
        }
        result = self.status_flags.process_bad_status_flags(data)

        expected = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 88, 'Quality': 29 },
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 88, 'Quality': 29 },
        ]
        self.assertEqual(result, expected)
    
    def test_process_bad_status_flags_with_first_and_third_diferent_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 88, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 64, 'Quality': 29 },
            ]
        }
        result = self.status_flags.process_bad_status_flags(data)

        expected = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 88, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 88, 'Quality': 29 },
        ]
        self.assertEqual(result, expected)
    
    def test_process_bad_status_flags_with_second_and_fourth_diferent_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 88, 'Quality': 29 },
            ]
        }
        result = self.status_flags.process_bad_status_flags(data)

        expected = [
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 88, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 88, 'Quality': 29 },
        ]
        self.assertEqual(result, expected)
    
    def test_process_bad_status_flags_with_third_and_fourth_diferent_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 88, 'Quality': 29 },
            ]
        }
        result = self.status_flags.process_bad_status_flags(data)

        expected = [
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 88, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 88, 'Quality': 29 },
        ]
        self.assertEqual(result, expected)
    
    def test_process_bad_status_flags_with_all_diferent_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 66, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 77, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 88, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
            ]
        }
        result = self.status_flags.process_bad_status_flags(data)

        expected = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 66, 'Quality': 29 },
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 66, 'Quality': 29 },
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 77, 'Quality': 29 },
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 77, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 88, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 88, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
        ]
        self.assertEqual(result, expected)

       