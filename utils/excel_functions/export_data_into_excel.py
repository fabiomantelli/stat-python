import datetime
import openpyxl
from openpyxl import Workbook

from .header_in_excel import header_in_excel
from .configure_pmu_summary_header import configure_pmu_summary_header
from .get_total_duration_of_status_flags import get_total_duration_of_status_flags
from .get_period_time_of_status_flags import get_period_time_of_status_flags


def export_data_into_excel(status_flags, pmu, date, server_name):
    month, day, year = date.split("-")

    if not status_flags:
        return
    try:
        file_name = f"./data/{year}_{month}_medfasee_{server_name}_status_flags.xlsx"
        workbook = openpyxl.load_workbook(file_name)
    except FileNotFoundError:
        workbook = Workbook()
    try:
        worksheet = workbook[pmu]
    except KeyError:
        worksheet = workbook.create_sheet(pmu)

    header_in_excel(worksheet, pmu)
    configure_pmu_summary_header(worksheet)

    get_period_time_of_status_flags(worksheet, status_flags, date)

    get_total_duration_of_status_flags(worksheet)
    workbook.save(file_name)
