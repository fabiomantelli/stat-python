import openpyxl
from utils.create_file_name import create_file_name

def update_síntese(pmu, date, server_name):

    file_name = create_file_name(date, server_name)
    workbook = openpyxl.load_workbook(file_name)
    worksheet = get_worksheet(workbook, pmu)

    if not worksheet:
        return

    freq_DE1F0, periodo_medio_DE1F0, periodo_total_DE1F0 = get_cell_values(worksheet, "DE1F0")
    freq_DE040, periodo_medio_DE040, periodo_total_DE040 = get_cell_values(worksheet, "DE040")
    freq_DE000, periodo_medio_DE000, periodo_total_DE000 = get_cell_values(worksheet, "DE000")

    status_flags_diferente, freq_status_flags_diferente, periodo_medio_status_flags_diferente, periodo_total_status_flags_diferente = get_status_flags_diferente(worksheet)

    workbook.save(file_name)
    
    write_síntese(workbook, pmu, freq_DE1F0, periodo_medio_DE1F0, periodo_total_DE1F0, freq_DE040,
                             periodo_medio_DE040, periodo_total_DE040, freq_DE000, periodo_medio_DE000,
                             periodo_total_DE000, freq_status_flags_diferente, periodo_medio_status_flags_diferente,
                             periodo_total_status_flags_diferente, server_name, date)


def get_worksheet(workbook, pmu):
    if pmu in workbook.sheetnames:
        return workbook[pmu]
    else:
        return None


def find_cell_value(sheet, target_value, col):    
    for row in sheet.iter_rows():
        for cell in row:
            if cell.column == col and cell.value == target_value:
                return cell
    return None


def get_cell_values(worksheet, cell_value):
    cell = find_cell_value(worksheet, cell_value, 9)
    if cell is not None:
        col = cell.column
        row = cell.row
        freq = worksheet.cell(row=row, column=col + 1).value
        periodo_medio = worksheet.cell(row=row, column=col + 2).value
        periodo_total = worksheet.cell(row=row, column=col + 3).value
    else:
        freq = 0
        periodo_medio = 0
        periodo_total = 0

    return freq, periodo_medio, periodo_total


def get_status_flags_diferente(worksheet):
    status_flags_diferente = 0
    column = worksheet['I']
    # Verificar se há valores diferentes de "DE1F0", "DE040" e "DE000" na coluna
    for cell in column:
        if cell.value and cell.value not in ['DE1F0', 'DE040', 'DE000', 'Status Flag']:
            status_flags_diferente = cell.value
            break

    freq_status_flags_diferente, periodo_medio_status_flags_diferente, periodo_total_status_flags_diferente = 0, 0, 0

    status_flags_diferente_cell = find_cell_value(worksheet, status_flags_diferente, 9)
    if status_flags_diferente_cell is not None:
        status_flags_diferente_col = status_flags_diferente_cell.column
        status_flags_diferente_row = status_flags_diferente_cell.row
        freq_status_flags_diferente = worksheet.cell(row=status_flags_diferente_row, column=status_flags_diferente_col + 1).value
        periodo_medio_status_flags_diferente = worksheet.cell(row=status_flags_diferente_row, column=status_flags_diferente_col + 2).value
        periodo_total_status_flags_diferente = worksheet.cell(row=status_flags_diferente_row, column=status_flags_diferente_col + 3).value

    return status_flags_diferente, freq_status_flags_diferente, periodo_medio_status_flags_diferente, periodo_total_status_flags_diferente


def write_síntese(workbook, pmu, freq_DE1F0, periodo_medio_DE1F0, periodo_total_DE1F0, freq_DE040,
                             periodo_medio_DE040, periodo_total_DE040, freq_DE000, periodo_medio_DE000,
                             periodo_total_DE000, freq_status_flags_diferente, periodo_medio_status_flags_diferente,
                             periodo_total_status_flags_diferente, server_name, date):
    worksheet1 = workbook['Síntese']
    worksheet_exists = 'Síntese' in workbook.sheetnames

    if worksheet_exists:
        identificacao = find_cell_value(worksheet1, pmu, 3)
        identificacao_col = identificacao.column
        identificacao_row = identificacao.row
        worksheet1.cell(row=identificacao_row, column=identificacao_col + 1).value = freq_DE1F0
        worksheet1.cell(row=identificacao_row, column=identificacao_col + 2).value = periodo_medio_DE1F0
        worksheet1.cell(row=identificacao_row, column=identificacao_col + 3).value = periodo_total_DE1F0
        worksheet1.cell(row=identificacao_row, column=identificacao_col + 4).value = freq_DE040
        worksheet1.cell(row=identificacao_row, column=identificacao_col + 5).value = periodo_medio_DE040
        worksheet1.cell(row=identificacao_row, column=identificacao_col + 6).value = periodo_total_DE040
        worksheet1.cell(row=identificacao_row, column=identificacao_col + 7).value = freq_DE000
        worksheet1.cell(row=identificacao_row, column=identificacao_col + 8).value = periodo_medio_DE000
        worksheet1.cell(row=identificacao_row, column=identificacao_col + 9).value = periodo_total_DE000
        worksheet1.cell(row=identificacao_row, column=identificacao_col + 10).value = freq_status_flags_diferente
        worksheet1.cell(row=identificacao_row, column=identificacao_col + 11).value = periodo_medio_status_flags_diferente
        worksheet1.cell(row=identificacao_row, column=identificacao_col + 12).value = periodo_total_status_flags_diferente

    workbook.save(create_file_name(date, server_name))
