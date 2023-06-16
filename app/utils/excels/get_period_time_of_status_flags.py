import datetime

from app.utils.convert_decimal_to_binary import convert_decimal_to_binary
from .format_time import format_time
from .get_time_duration import get_time_duration

def get_period_time_of_status_flags(worksheet, status_flags, date):
    last_row = worksheet.max_row
    while worksheet.cell(row=last_row, column=2).value is None:
        last_row -= 1
    increment_by_two = range(0, len(status_flags), 2)
    for current_excel_line, item in enumerate(increment_by_two, start=last_row + 1):
        worksheet.insert_rows(current_excel_line)
        NUMBER_COLUMN = 1
        worksheet.cell(row=current_excel_line, column=NUMBER_COLUMN).value = current_excel_line - 2
        DATE_COLUMN = 2
        worksheet.cell(row=current_excel_line, column=DATE_COLUMN).value = datetime.datetime.strptime(
            date, '%m-%d-%y').strftime('%d/%m/%Y')
        STATUS_FLAGS_HEX_COLUMN = 3
        worksheet.cell(row=current_excel_line, column=STATUS_FLAGS_HEX_COLUMN).value = hex(
            status_flags[item]['Value'])[2:].upper()
        STATUS_FLAGS_BINARY_COLUMN = 4
        worksheet.cell(row=current_excel_line, column=STATUS_FLAGS_BINARY_COLUMN).value = convert_decimal_to_binary(
            status_flags, item)
        START_TIME_COLUMN = 5
        start_time = status_flags[item]['Time']
        worksheet.cell(row=current_excel_line, column=START_TIME_COLUMN).value = format_time(start_time)
        END_TIME_COLUMN = 6
        end_time = status_flags[item + 1]['Time']
        worksheet.cell(row=current_excel_line, column=END_TIME_COLUMN).value = format_time(end_time)
        PERIOD_COLUMN = 7
        duration_time = get_time_duration(start_time, end_time)
        worksheet.cell(row=current_excel_line, column=PERIOD_COLUMN).value = duration_time
        START_TIME_COLUMN = 5
        cell_start_time = worksheet.cell(row=current_excel_line, column=START_TIME_COLUMN)
        cell_start_time.number_format = "h:mm:ss.000"
