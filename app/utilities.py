import datetime
from datetime import datetime

def convert_decimal_to_binary(status_flags):
    binary_status_flags = bin(status_flags[0]['Value']).zfill(20)[2:]
    return ' '.join(binary_status_flags[i:i+4] for i in range(0, len(binary_status_flags), 4))

def format_time(time_str):
    time_obj = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
    formatted_time = time_obj.strftime("%H:%M:%S.%f")[:-3]
    return formatted_time

def elapsed_time(request_start_time, request_end_time):
    elapsed_time_in_minutes = (request_end_time - request_start_time) // 60
    elapsed_time_in_seconds = (request_end_time - request_start_time) % 60
    print(
        f"[Elapsed time] {int(elapsed_time_in_minutes)} minutes and {int(elapsed_time_in_seconds)} seconds \n")

def get_time_duration(start_time, end_time):
    parsed_start_time = datetime.datetime.strptime(
        start_time, "%Y-%m-%d %H:%M:%S.%f")
    parsed_end_time = datetime.datetime.strptime(
        end_time, "%Y-%m-%d %H:%M:%S.%f")
    duration = (parsed_end_time - parsed_start_time).total_seconds()
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = round((seconds - int(seconds)) * 1000)
    duration_str = "{:02d}:{:02d}:{:02d}.{:03d}".format(
        int(hours), int(minutes), int(seconds), milliseconds)
    return duration_str

def set_datetime(date, time):
    try:
        datetime.strptime(date, '%m-%d-%y')
    except ValueError:
        return f"{date} is not a valid date."
    return f"{date} {time}"