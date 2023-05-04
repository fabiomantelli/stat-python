import time
import requests
import json
from datetime import datetime, timedelta

from utils.process_data import process_data
from utils.export_data_into_excel import export_data_into_excel
from utils.create_excel_file import create_excel_file
from utils.elapsed_time import elapsed_time

from models.ppa_status_flags import ppa_status_flags

# date = '05-03-23'
today = datetime.today()
yesterday = today - timedelta(days=1)
formatted_yesterday = yesterday.strftime("%m-%d-%y")

server = '150.162.19.214'
# startTime = f'{date} 18:45:00.000'
# endTime = f'{date} 18:49:00.000'
startTime = f'{formatted_yesterday} 00:00:00.000'
endTime = f'{formatted_yesterday} 23:59:59.999'

for item in ppa_status_flags:
    start_time = time.time()

    pmu = item['pmu']
    statusFlags = item['statusFlags']

    url = f'http://{server}:6152/historian/timeseriesdata/read/historic/{statusFlags}/{startTime}/{endTime}/json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text
        my_dict = json.loads(data)

        status_flags = process_data(my_dict)
        print('\n')
        print(f'[{pmu}] status_flags:{status_flags}')
        create_excel_file(formatted_yesterday)
        export_data_into_excel(status_flags, pmu, formatted_yesterday)

    else:
        print(f"Error: Failed to retrieve data from {url}")

    end_time = time.time()
    elapsed_time(start_time, end_time)

    # wait before making the next request
    time.sleep(1)
