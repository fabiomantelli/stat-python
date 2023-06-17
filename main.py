import time
import sys
import requests
import json

from datetime import datetime, timedelta
from app.utils.process_bad_status_flags import process_bad_status_flags
from app.utils.excel_handler import export_data_into_excel
from app.utils.excel_handler import create_excel_file
from app.utils.elapsed_time import elapsed_time
from app.utils.get_servers import get_server
from app.utils.set_datetime import set_datetime
from app.utils.ppa_status_flags import ppa_status_flags

def main():
    server_name = "ons_pdcmi_rj"
    server = get_server(server_name)
    port = ppa_status_flags[server_name]['port']

    if server is None:
        print(f"There is no {server_name} in ppa_status_flags.")
        sys.exit()

    date = '06-02-23'
    start_time = '04:41:00.000'
    end_time = '04:44:59.999'
    #start_time = "00:00:00.000"
    #end_time = "23:59:59.999"
    yesterday = datetime.today() - timedelta(days=1)
    formatted_yesterday = yesterday.strftime("%m-%d-%y")
    start_time = set_datetime(formatted_yesterday, start_time)
    end_time = set_datetime(formatted_yesterday, end_time)

    for item in ppa_status_flags[server_name]['ppa']:
        initial_test_time = time.time()
        pmu = item['pmu']
        statusFlags = item['statusFlags']
        url = f'http://{server}:{port}/historian/timeseriesdata/read/historic/{statusFlags}/{start_time}/{end_time}/json'
        response = requests.get(url)
        REQUEST_SUCCEEDED = 200
        if response.status_code == REQUEST_SUCCEEDED:
            data = response.text
            data_json = json.loads(data)
            status_flags = process_bad_status_flags(data_json)
            print(f'[{pmu.upper()}] status_flags: {status_flags}')
            create_excel_file(date, server_name)
            export_data_into_excel(
                status_flags, pmu, date, server_name)
        else:
            print(f"Error: Failed to retrieve data from {url}")
        end_test_time = time.time()
        elapsed_time(initial_test_time, end_test_time)
        time.sleep(1)

main()
