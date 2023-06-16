TOTAL_PERIOD_COLUMN = 12
FREQUENCY_COLUMN = 10
def get_average_period(worksheet):
    average_period = worksheet.cell(row=3, column=TOTAL_PERIOD_COLUMN).value
    frequency = worksheet.cell(row=3, column=FREQUENCY_COLUMN).value
    return average_period / frequency
