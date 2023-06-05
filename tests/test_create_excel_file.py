import unittest
import os

from utils.excel_functions.create_excel_file import create_excel_file

class TestCreateExcel(unittest.TestCase):

    def test_create_excel_file_if_model_file_exists(self):
        file = "./data/model.xlsx"
        date = '01-01-01'
        server_name = "brazil"
        create_excel_file(date, server_name)
        self.assertEqual(os.path.isfile(file), True)

    def test_create_excel_file_if_file_is_create(self):
        date = '05-01-22'
        server_name = "brazil"
        excel_file_name = "./data/22_05_medfasee_brazil_status_flags.xlsx"
        create_excel_file(date, server_name)
        self.assertEqual(os.path.isfile(excel_file_name), True)

