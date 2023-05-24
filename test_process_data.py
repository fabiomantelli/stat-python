import unittest
from utils.process_data import process_data

class TestProcessData(unittest.TestCase):
    
    def test_process_data_with_empty_dict(self):
        data = {
            "TimeSeriesDataPoints": []
        }
        result = process_data(data)
        self.assertEqual(result, [])
    
    
    def test_process_data_with_no_bad_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 0, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 557056, 'Quality': 29 },
            ]
        }
        result = process_data(data)
        self.assertEqual(result, [])
    
    def test_process_data_with_single_first_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 64, 'Quality': 29 },
            ]
        }
        result = process_data(data)

        status_flags = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
        ]
        self.assertEqual(result, status_flags)
    
    def test_process_data_with_single_last_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            ]
        }
        result = process_data(data)

        status_flags = [
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
        ]
        self.assertEqual(result, status_flags)
    
    def test_process_data_with_single_first_and_single_last_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            ]
        }
        result = process_data(data)

        status_flags = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
        ]
        self.assertEqual(result, status_flags)
    
    def test_process_data_with_two_firsts_and_single_last_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
            ]
        }
        result = process_data(data)

        status_flags = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
        ]
        self.assertEqual(result, status_flags)
    
    def test_process_data_with_first_and_two_lasts_point_with_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
            ]
        }
        result = process_data(data)

        status_flags = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
        ]
        self.assertEqual(result, status_flags)
    
    def test_process_data_with_first_and_second_diferent_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 88, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 64, 'Quality': 29 },
            ]
        }
        result = process_data(data)

        status_flags = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 88, 'Quality': 29 },
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 88, 'Quality': 29 },
        ]
        self.assertEqual(result, status_flags)
    
    def test_process_data_with_first_and_third_diferent_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 88, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 64, 'Quality': 29 },
            ]
        }
        result = process_data(data)

        status_flags = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 88, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 88, 'Quality': 29 },
        ]
        self.assertEqual(result, status_flags)
    
    def test_process_data_with_second_and_fourth_diferent_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 88, 'Quality': 29 },
            ]
        }
        result = process_data(data)

        status_flags = [
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 88, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 88, 'Quality': 29 },
        ]
        self.assertEqual(result, status_flags)
    
    def test_process_data_with_third_and_fourth_diferent_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 64, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 88, 'Quality': 29 },
            ]
        }
        result = process_data(data)

        status_flags = [
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 88, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 88, 'Quality': 29 },
        ]
        self.assertEqual(result, status_flags)
    
    def test_process_data_with_all_diferent_status_flags(self):
        data = {
            "TimeSeriesDataPoints": [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 66, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 77, 'Quality': 29 },
                {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 88, 'Quality': 29 },
                {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
            ]
        }
        result = process_data(data)

        status_flags = [
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 66, 'Quality': 29 },
            {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 66, 'Quality': 29 },
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 77, 'Quality': 29 },
            {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 77, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 88, 'Quality': 29 },
            {"HistorianID": 3, 'Time': '2023-05-03 00:00:00.300', 'Value': 88, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
            {"HistorianID": 4, 'Time': '2023-05-03 00:00:00.400', 'Value': 99, 'Quality': 29 },
        ]
        self.assertEqual(result, status_flags)