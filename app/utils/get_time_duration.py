import datetime

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
