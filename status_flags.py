import time
import sys
import requests
import json
from datetime import datetime, timedelta

from utils.process_data import process_data
from utils.export_data_into_excel import export_data_into_excel
from utils.create_excel_file import create_excel_file
from utils.elapsed_time import elapsed_time
from utils.get_servers import get_server
from utils.formatting import formatting


from models.ppa_status_flags import ppa_status_flags

date = '05-12-23'
today = datetime.today()
yesterday = today - timedelta(days=1)
formatted_yesterday = yesterday.strftime("%m-%d-%y")

server_name = "brazil"
server = get_server(server_name)

if server is None:
    print(f"There is no {server_name} in ppa_status_flags.")
    sys.exit()
else:
    startTime = f'{date} 00:44:00.000'
    endTime = f'{date} 00:45:00.000'
    #startTime = f'{date} 00:00:00.000'
    #endTime = f'{date} 23:59:59.000'
    #startTime = f'{formatted_yesterday} 00:00:00.000'
    #endTime = f'{formatted_yesterday} 23:59:59.999'

    for item in ppa_status_flags[server_name]['ppa']:
        start_time = time.time()

        pmu = item['pmu']
        statusFlags = item['statusFlags']

        url = f'http://{server}:6152/historian/timeseriesdata/read/historic/{statusFlags}/{startTime}/{endTime}/json'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.text
            data_json = json.loads(data)

            status_flags = process_data(data_json)
            print(f'[{pmu.upper()}] status_flags: {status_flags}')
            create_excel_file(date, server_name)
            export_data_into_excel(
                status_flags, pmu, date, server_name)

        else:
            print(f"Error: Failed to retrieve data from {url}")

        end_time = time.time()
        elapsed_time(start_time, end_time)

        # wait before making the next request
        time.sleep(1)

    for item in ppa_status_flags[server_name]['ppa']:
        if 'pmu' in item:
            pmu = item['pmu']
            formatting(pmu, date, server_name)