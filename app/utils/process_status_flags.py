import json
import sys
import time
from datetime import timedelta, datetime

import requests

from app.utils.process_bad_status_flags import process_bad_status_flags
from app.utils.elapsed_time import elapsed_time
from app.utils.ppa_status_flags import ppa_status_flags
from app.utils.set_datetime import set_datetime
from app.utils.excel_handler import export_data_into_excel
from app.utils.excel_handler import ExcelHandler
from app.utils.get_servers import get_server
from app.utils.status_flags_repository_api import StatusFlagsRepositoryApi

class ProcessStatusFlags:
    def __init__(self, server_name, port, date, start_time, end_time):
        self.server_name = server_name
        self.port = port
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def execute(self):
        server = get_server(self.server_name)
        if server is None:
            print(f"There is no {self.server_name} in ppa_status_flags.")
            sys.exit()
        yesterday = datetime.today() - timedelta(days=1)
        formatted_yesterday = yesterday.strftime("%m-%d-%y")
        start_time = set_datetime(self.date, self.start_time)
        end_time = set_datetime(self.date, self.end_time)
        for item in ppa_status_flags[self.server_name]['ppa']:
            initial_test_time = time.time()
            pmu = item['pmu']
            status_flags_ppa = item['status_flags_ppa']
            try:
                status_flags_repository_api = StatusFlagsRepositoryApi(server, self.port, status_flags_ppa, start_time, end_time)
                data_json = status_flags_repository_api.get()
                status_flags = process_bad_status_flags(data_json)
                print(f'[{pmu.upper()}] status_flags: {status_flags}')
                create_excel_file = ExcelHandler(self.date, self.server_name)
                export_data_into_excel(
                    status_flags, pmu, self.date, self.server_name)
                end_test_time = time.time()
                elapsed_time(initial_test_time, end_test_time)
                time.sleep(1)
            except Exception as e:
                print("An error occurred:", e)