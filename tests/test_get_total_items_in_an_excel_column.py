import unittest
from unittest.mock import MagicMock

from app.utils.get_total_items_in_a_excel_column import get_total_items_in_an_excel_column

# class TestGetTotalItemsInAnExcelColumn(unittest.TestCase):

#     def test_get_total_items_in_an_excel_column_if_have_two_lines(self):
#         mock_worksheet = MagicMock()

#         column_values = ['DE1F0', 'DDE040']
#         STATUS_FLAGS_COLUMN = 3
#         START_ROW = 3
#         mock_worksheet.__getitem__.return_value = column_values

#         line_count = get_total_items_in_an_excel_column(mock_worksheet, STATUS_FLAGS_COLUMN, START_ROW)
#         expecte_line_count = len(column_values) - 2
#         self.assertEqual(line_count, expecte_line_count)