import datetime

from utils.convert_decimal_to_binary import convert_decimal_to_binary
from .format_time import format_time
from .get_time_duration import get_time_duration


def get_period_time_of_status_flags(worksheet, status_flags, date):
    last_row = worksheet.max_row
    while worksheet.cell(row=last_row, column=2).value is None:
        last_row -= 1

    increment_by_two = range(0, len(status_flags), 2)
    for line_number, item in enumerate(increment_by_two, start=last_row + 1):
        worksheet.insert_rows(line_number)
        worksheet.cell(row=line_number, column=1).value = line_number - 2
        worksheet.cell(row=line_number, column=2).value = datetime.datetime.strptime(
            date, '%m-%d-%y').strftime('%d/%m/%Y')
        worksheet.cell(row=line_number, column=3).value = hex(
            status_flags[item]['Value'])[2:].upper()
        worksheet.cell(row=line_number, column=4).value = convert_decimal_to_binary(
            status_flags, item)

        start_time = status_flags[item]['Time']
        end_time = status_flags[item + 1]['Time']

        worksheet.cell(row=line_number,
                       column=5).value = format_time(start_time)
        worksheet.cell(row=line_number, column=6).value = format_time(end_time)

        duration_time = get_time_duration(start_time, end_time)

        PERIOD_COLUMN = 7
        worksheet.cell(row=line_number,
                       column=PERIOD_COLUMN).value = duration_time

        START_TIME_COLUMN = 5
        cell_start_time = worksheet.cell(
            row=line_number, column=START_TIME_COLUMN)
        cell_start_time.number_format = "h:mm:ss.000"
