import unittest
import os

from app.utils.excel_handler import create_excel_file

class TestExcelHandler(unittest.TestCase):

    def test_create_excel_file_if_model_file_exists(self):
        file = "./exports/model_ons_pdcmi_bsb.xlsx"
        date = '01-01-01'
        server_name = "brazil"
        create_excel_file(date, server_name)
        self.assertEqual(os.path.isfile(file), True)

    def test_create_excel_file_if_file_is_create(self):
        date = '05-01-22'
        server_name = "ons_pdcmi_bsb"
        excel_file_name = "./exports/22_05_ons_pdcmi_bsb_status_flags.xlsx"
        create_excel_file(date, server_name)
        self.assertEqual(os.path.isfile(excel_file_name), True)