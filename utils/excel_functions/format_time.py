import datetime

def format_time(time_str):
    time_obj = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
    formatted_time = time_obj.strftime("%H:%M:%S.%f")[:-3]
    return formatted_time