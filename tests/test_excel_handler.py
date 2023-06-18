import unittest
import os

from app.utils.excel_handler import ExcelHandler

class TestExcelHandler(unittest.TestCase):
    def setUp(self):
        self.date = '01-01-01'
        self.server_name = "brazil"
        self.excel_handler = ExcelHandler(self.date, self.server_name)

    def test_create_excel_file_if_model_file_exists(self):
        file = "./exports/model_brazil.xlsx"
        self.excel_handler.create_excel_file(self.date, self.server_name)
        self.assertEqual(os.path.isfile(file), True)

    def test_create_excel_file_if_file_is_create(self):
        excel_file_name = "./exports/01_01_brazil_status_flags.xlsx"
        self.excel_handler.create_excel_file(self.date, self.server_name)
        self.assertEqual(os.path.isfile(excel_file_name), True)