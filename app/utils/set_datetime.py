from datetime import datetime

def set_datetime(date, time):
    try:
        datetime.strptime(date, '%m-%d-%y')
    except ValueError:
        return f"{date} is not a valid date."
    return f"{date} {time}"