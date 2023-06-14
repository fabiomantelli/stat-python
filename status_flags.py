import time
import sys
import requests
import json
from datetime import datetime, timedelta

from utils.process_data import process_data
from utils.excel_functions.export_data_into_excel import export_data_into_excel
from utils.excel_functions.create_excel_file import create_excel_file
from utils.elapsed_time import elapsed_time
from utils.get_servers import get_server

from models.ppa_status_flags import ppa_status_flags

date = '06-03-23'
today = datetime.today()
yesterday = today - timedelta(days=1)
formatted_yesterday = yesterday.strftime("%m-%d-%y")

server_name = "ons_pdcmi_bsb"
server = get_server(server_name)

if server is None:
    print(f"There is no {server_name} in ppa_status_flags.")
    sys.exit()

#start_time = f'{date} 00:00:00.000'
#end_time = f'{date} 00:01:59.000'
start_time = f'{formatted_yesterday} 00:00:00.000'
end_time = f'{formatted_yesterday} 23:59:59.999'

for item in ppa_status_flags[server_name]['ppa']:
    request_start_time = time.time()

    pmu = item['pmu']
    statusFlags = item['statusFlags']

    url = f'http://{server}:6152/historian/timeseriesdata/read/historic/{statusFlags}/{start_time}/{end_time}/json'
    response = requests.get(url)

    REQUEST_SUCCEEDED = 200
    if response.status_code == REQUEST_SUCCEEDED:
        data = response.text
        data_json = json.loads(data)

        status_flags = process_data(data_json)
        print(f'[{pmu.upper()}] status_flags: {status_flags}')

        create_excel_file(date, server_name)
        export_data_into_excel(
            status_flags, pmu, date, server_name)
    else:
        print(f"Error: Failed to retrieve data from {url}")

    request_end_time = time.time()
    elapsed_time(request_start_time, request_end_time)

    time.sleep(1)
