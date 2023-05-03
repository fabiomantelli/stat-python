import requests
import json
import pandas as pd

ppa = [
    {id: '2', 'pmu': 'ufpa', 'statusFlags': 159},
    {id: '3', 'pmu': 'unifei', 'statusFlags': 204},
    {id: '4', 'pmu': 'unb', 'statusFlags': 249},
    {id: '5', 'pmu': 'coppe', 'statusFlags': 3972},
    {id: '6', 'pmu': 'usp-sc', 'statusFlags': 2146},
    {id: '13', 'pmu': 'ufmg', 'statusFlags': 523},
    {id: '25', 'pmu': 'ufjf', 'statusFlags': 662}
]

date = '05-03-23'
server = '150.162.19.214'
startTime = f'{date} 18:45:00.000'
endTime = f'{date} 18:49:00.000'

url = f'http://{server}:6152/historian/timeseriesdata/read/historic/887/{startTime}/{endTime}/json'
response = requests.get(url)

if response.status_code == 200:
    data = response.text
    my_dict = json.loads(data)

else:
    print("Error: Failed to retrieve data from openPDC URL")


def is_bad_status_flags(status):
    if status != 64:
        return True
    else:
        return False


status_flags = []
flag = False

for item in my_dict['TimeSeriesDataPoints']:
    historian_id = item['HistorianID']
    value = item['Value']
    # apply filter to value and convert filter object to list
    filtered_value = is_bad_status_flags(value)

    if (flag is False and filtered_value is True):
        status_flags.append(item)
        flag = True

    elif (flag is True and filtered_value is False):
        status_flags.append(temporary)
        flag = False
    elif (flag is True and value != temporary['Value']):
        status_flags.append(temporary)
        status_flags.append(item)

    temporary = item


print('--------')
print(f'flags:{status_flags}')

two_by_two = [(status_flags[i]['Value'], status_flags[i]['Time'], status_flags[i+1]['Time'])
              for i in range(0, len(status_flags), 2)]

df = pd.DataFrame(two_by_two, columns=['Value', 'Initial Time', 'Final Time'])

with pd.ExcelWriter('time_pairs.xlsx') as writer:
    df.to_excel(writer, index=False)
