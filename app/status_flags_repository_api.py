import json
import requests

class StatusFlagsRepositoryApi:
    def __init__(self, server, port, status_flags_ppa, start_time, end_time):
        self.server = server
        self.port = port
        self.status_flags_ppa = status_flags_ppa
        self.start_time = start_time
        self.end_time = end_time

    def get(self):
        try:
            url = f'http://{self.server}:{self.port}/historian/timeseriesdata/read/historic/{self.status_flags_ppa}/{self.start_time}/{self.end_time}/json'
            response = requests.get(url)
            data = response.text
            data_json = json.loads(data)
            return data_json
        except requests.exceptions.RequestException as e:
            print("An error occurred during the API request:", e)