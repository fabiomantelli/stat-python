NUM_COLUMN = 2
IDENTIFICATION_COLUMN = 3
FREQUENCY_COLUMN = 4
AVERAGE_DURATION_COLUMN = 5
TOTAL_DURATION_COLUMN = 6
def set_summary_header(worksheet):
    worksheet.cell(row=2, column=NUM_COLUMN, value='ID Code')
    worksheet.cell(row=2, column=IDENTIFICATION_COLUMN, value='Identificação')
    worksheet.cell(row=2, column=FREQUENCY_COLUMN, value='Frequência de ocorrências DE1F0')
    worksheet.cell(row=2, column=AVERAGE_DURATION_COLUMN, value='Duração Média')
    worksheet.cell(row=2, column=TOTAL_DURATION_COLUMN, value='Duração total')
    worksheet.cell(row=2, column=FREQUENCY_COLUMN+3, value='Frequência de ocorrências DE040')
    worksheet.cell(row=2, column=AVERAGE_DURATION_COLUMN+3, value='Duração Média')
    worksheet.cell(row=2, column=TOTAL_DURATION_COLUMN+3, value='Duração total')
    worksheet.cell(row=2, column=FREQUENCY_COLUMN+6, value='Frequência de ocorrências OUTROS')
    worksheet.cell(row=2, column=AVERAGE_DURATION_COLUMN+6, value='Duração Média')
    worksheet.cell(row=2, column=TOTAL_DURATION_COLUMN+6, value='Duração total')