import unittest
from unittest import mock
from datetime import datetime, timedelta, time

from app.excel_handler import ExcelHandler

class TestGetAveragePeriod(unittest.TestCase):

    def test_get_average_period_if_has_two_frequencies(self):
        excel_handler = ExcelHandler("01-01-21", "brazil")
        mock_worksheet = mock.MagicMock()
        average_period_cell = mock.MagicMock()
        average_period_cell.value = timedelta(milliseconds=500)
        
        frequency_cell = mock.MagicMock()
        frequency_cell.value = 2
        mock_worksheet.cell.side_effect = [average_period_cell, frequency_cell]

        result = excel_handler.get_average_period(mock_worksheet)

        self.assertEqual(result, timedelta(milliseconds=250))
