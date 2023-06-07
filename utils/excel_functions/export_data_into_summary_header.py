def export_data_into_summary_header(worksheet, sintese_worksheet, pmu):
    for row in sintese_worksheet.iter_rows():
        for cell in row:
            if cell.value == pmu:
                STATUS_FLAGS_COLUMN = 9
                if worksheet.cell(row=3, column=STATUS_FLAGS_COLUMN).value == 'DE1F0':
                    FREQUENCY_COLUMN = 10
                    sintese_worksheet.cell(row=cell.row, column=cell.column + 1).value = worksheet.cell(row=3, column=FREQUENCY_COLUMN).value
                    AVERAGE_PERIOD_COLUMN = 11
                    sintese_worksheet.cell(row=cell.row, column=cell.column + 2).value = worksheet.cell(row=3, column=AVERAGE_PERIOD_COLUMN).value
                    TOTAL_PERIOD_COLUMN = 12
                    sintese_worksheet.cell(row=cell.row, column=cell.column + 3).value = worksheet.cell(row=3, column=TOTAL_PERIOD_COLUMN).value
                elif worksheet.cell(row=3, column=STATUS_FLAGS_COLUMN).value == 'DE040':
                    FREQUENCY_COLUMN = 10
                    sintese_worksheet.cell(row=cell.row, column=cell.column + 4).value = worksheet.cell(row=3, column=FREQUENCY_COLUMN).value
                    AVERAGE_PERIOD_COLUMN = 11
                    sintese_worksheet.cell(row=cell.row, column=cell.column + 5).value = worksheet.cell(row=3, column=AVERAGE_PERIOD_COLUMN).value
                    TOTAL_PERIOD_COLUMN = 12
                    sintese_worksheet.cell(row=cell.row, column=cell.column + 6).value = worksheet.cell(row=3, column=TOTAL_PERIOD_COLUMN).value
                else:
                    FREQUENCY_COLUMN = 10
                    sintese_worksheet.cell(row=cell.row, column=cell.column + 7).value = worksheet.cell(row=3, column=FREQUENCY_COLUMN).value
                    AVERAGE_PERIOD_COLUMN = 11
                    sintese_worksheet.cell(row=cell.row, column=cell.column + 8).value = worksheet.cell(row=3, column=AVERAGE_PERIOD_COLUMN).value
                    TOTAL_PERIOD_COLUMN = 12
                    sintese_worksheet.cell(row=cell.row, column=cell.column + 9).value = worksheet.cell(row=3, column=TOTAL_PERIOD_COLUMN).value