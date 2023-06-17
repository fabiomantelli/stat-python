import unittest
from app.utils.convert_decimal_to_binary import convert_decimal_to_binary

class TestConvertDecimalToBinary(unittest.TestCase):

    def test_convert_decimal_to_binary_with_spaces_between_four_digits(self):
        status_flags = [
                {"HistorianID": 1, 'Time': '2023-05-03 00:00:00.100', 'Value': 909312, 'Quality': 29 },
                {"HistorianID": 2, 'Time': '2023-05-03 00:00:00.200', 'Value': 909312, 'Quality': 29 }
            ]

        result = convert_decimal_to_binary(status_flags)
        self.assertEqual(result, "1101 1110 0000 0000 0000")