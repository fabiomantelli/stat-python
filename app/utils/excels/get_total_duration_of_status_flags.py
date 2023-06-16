import datetime

def get_total_duration_of_status_flags(worksheet):
    PERIOD_COLUMN = 7
    total_duration = datetime.timedelta()
    for row in range(3, worksheet.max_row + 1):
        cell_value = worksheet.cell(row=row, column=PERIOD_COLUMN).value
        if cell_value is not None:
            time_value = datetime.datetime.strptime(
                cell_value, "%H:%M:%S.%f")
            time_delta = datetime.timedelta(hours=time_value.hour, minutes=time_value.minute,
                                            seconds=time_value.second, microseconds=time_value.microsecond)
            total_duration += time_delta
    return total_duration
