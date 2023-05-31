import datetime
import openpyxl


from openpyxl.styles.alignment import Alignment
from openpyxl.styles.borders import Border, Side
from openpyxl.styles import PatternFill 

def find_cell_value(sheet, target_value, col):
    # Encontra a posição da célula com o valor desejado na coluna especificada
    for row in sheet.iter_rows():
        for cell in row:
            if cell.column == col and cell.value == target_value:
                return cell
    return None


def formatting(pmu, date, server_name):
    parts = date.split("-")

    year = parts[2]
    month = parts[0]

    file_name = f"./data/{year}_{month}_medfasee_{server_name}_status_flags.xlsx"
    
    workbook = openpyxl.load_workbook(file_name)  

    worksheet_exists = pmu in workbook.sheetnames

    if worksheet_exists:
        worksheet = workbook[pmu]
    else:
        return
                  
    # Ajustar automaticamente o tamanho das colunas
    for col in ['A', 'B', 'E', 'F', 'G']:
        worksheet.column_dimensions[col].auto_size = True
        worksheet.column_dimensions['D'].width = 30
        worksheet.column_dimensions['C'].width = 30
        worksheet.column_dimensions['I'].width = 15
        worksheet.column_dimensions['J'].width = 12
        worksheet.column_dimensions['K'].width = 15
        worksheet.column_dimensions['L'].width = 15

    workbook.save(file_name)

    color_fill = PatternFill(start_color='FF0070C0', end_color='FF0070C0', fill_type='solid')    
    for cell in worksheet["1:1"]:
        cell.alignment = Alignment(horizontal='center')
        cell.font = cell.font.copy(bold=True, size=12, name='Arial')
        cell.fill = color_fill
        if cell.value is not None:
            cell.value = cell.value.upper()


    workbook.save(file_name)

    # Centralizar conteúdo das células a partir da linha 2    
    for row in worksheet.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(horizontal='center')

    
    # Gerar as colunas com as tabelas
    worksheet = worksheet
    if  worksheet_exists:
        worksheet['I2'] = "Status Flag"
        worksheet['J2'] = "Frequência"
        worksheet['K2'] = "Período médio"
        worksheet['L2'] = "Período total"

    color_fill = PatternFill(start_color='ADD8E6', end_color='ADD8E6', fill_type='solid')    
    for col in range(9, 13):
        cell = worksheet.cell(row=2, column=col)
        cell.fill = color_fill      
            
    # Centralizar as colunas I, J, K e L
    for col in worksheet.iter_cols(min_col=9):
        for cell in col:
            cell.alignment = Alignment(horizontal='center')
    # Define um dicionário para armazenar os grupos de linhas por valores únicos na coluna 3
    groups = {}

    # Percorre as células da coluna 3, a partir da terceira linha
    for row in range(3, worksheet.max_row + 1):
        # Obtém o valor da célula na coluna 3
        cell_value = worksheet.cell(row=row, column=3).value

        # Se o valor não for nulo, adiciona a linha ao grupo correspondente
        if cell_value is not None:
            if cell_value not in groups:
                groups[cell_value] = []
            groups[cell_value].append(row)

    # Percorre cada grupo de linhas e calcula a soma das horas
    for group in groups.values():
        # Define uma variável de soma para o grupo
        total_duration = 0

        # Percorre as linhas do grupo e adiciona as durações à variável de soma
        for row in group:
            # Obtém o valor da célula na coluna 7
            cell_value = worksheet.cell(row=row, column=7).value

            # Se o valor não for nulo, converte para um valor numérico e adiciona à variável de soma
            if cell_value is not None:
                duration_parts = cell_value.split(':')
                hours = int(duration_parts[0])
                minutes = int(duration_parts[1])
                seconds = int(duration_parts[2].split('.')[0])
                milliseconds = int(duration_parts[2].split('.')[1])
                total_duration += (hours * 3600) + (minutes * 60) + seconds + (milliseconds / 1000)

        # Converte a soma de segundos em um objeto timedelta
        td = datetime.timedelta(seconds=total_duration)

        # Formata o resultado usando strftime
        formatted_duration = "{:02d}:{:02d}:{:02d}.{:03d}".format(td.seconds // 3600, (td.seconds // 60) % 60, td.seconds % 60, td.microseconds // 1000)

        # Escreve o valor da soma na célula correspondente na coluna 12
        worksheet.cell(row=group[0], column=12).value = formatted_duration

    # Define um dicionário para armazenar a soma das durações e o número de ocorrências de cada elemento na coluna 3
    element_durations = {}

    # Percorre as células da coluna 7, a partir da terceira linha
    for row in range(3, worksheet.max_row + 1):
        # Obtém o valor da célula na coluna 3
        element_value = worksheet.cell(row=row, column=3).value

        # Obtém o valor da célula na coluna 7
        cell_value = worksheet.cell(row=row, column=7).value

        # Se o valor não for nulo, converte para um valor numérico e adiciona à variável de soma
        if cell_value is not None:
            duration_parts = cell_value.split(':')
            hours = int(duration_parts[0])
            minutes = int(duration_parts[1])
            seconds = int(duration_parts[2].split('.')[0])
            milliseconds = int(duration_parts[2].split('.')[1])
            total_duration = (hours * 3600) + (minutes * 60) + seconds + (milliseconds / 1000)

            # Se o elemento ainda não estiver no dicionário, adiciona com a duração atual e o número de ocorrências 1
            if element_value not in element_durations:
                element_durations[element_value] = {"total_duration": total_duration, "count": 1}
            # Se o elemento já estiver no dicionário, atualiza a duração total e o número de ocorrências
            else:
                element_durations[element_value]["total_duration"] += total_duration
                element_durations[element_value]["count"] += 1

    # Percorre o dicionário para calcular o período médio de cada elemento
    for element, durations in element_durations.items():
        average_duration = durations["total_duration"] / durations["count"]
        # Converte a duração média em um objeto timedelta
        td = datetime.timedelta(seconds=average_duration)
        # Formata o resultado usando strftime
        formatted_duration = "{:02d}:{:02d}:{:02d}.{:03d}".format(td.seconds // 3600, (td.seconds // 60) % 60, td.seconds % 60, td.microseconds // 1000)
        # Escreve o valor da duração média na célula correspondente na coluna 11
        worksheet.cell(row=3 + list(element_durations.keys()).index(element), column=11).value = formatted_duration
    

    # seleciona os valores únicos da coluna C a partir da linha 3
    valores_unicos = set()
    for row in worksheet.iter_rows(min_row=3, min_col=3, values_only=True):
        valores_unicos.add(row[0])

    # cria um dicionário para armazenar os valores únicos e suas frequências
    valores_e_frequencias = {}
    for valor in valores_unicos:
        frequencia = 0
        for row in worksheet.iter_rows(min_row=3, min_col=3, values_only=True):
            if row[0] == valor:
                frequencia += 1
        valores_e_frequencias[valor] = frequencia

    # escreve os valores e suas frequências nas colunas I e J
    cont = 0
    for row in worksheet.iter_rows(min_row=3):
        valor = row[2].value
        frequencia = valores_e_frequencias[valor]
        row[8].value = valor
        row[9].value = frequencia
        workbook.save(file_name)
        cont += 1
        if cont == len(valores_unicos):
            workbook.save(file_name)
            break

    # Aplicar bordas em todas as células da planilha que possuem valor
    for row in worksheet.iter_rows():
        for cell in row:
            if cell.value:
                cell.border = Border(
                    left=Side(style='thin', color='000000'),
                    right=Side(style='thin', color='000000'),
                    top=Side(style='thin', color='000000'),
                    bottom=Side(style='thin', color='000000')
                )
                
   # Configuração da borda vazia
    empty_border = Border()

    # Percorre todas as células na planilha
    for row in worksheet.iter_rows():
        for cell in row:
            # Verifica se a célula está vazia
            if cell.value is None or cell.value == "":
                # Remove a borda da célula vazia
                cell.border = empty_border

            
    workbook.save(file_name)

        
    worksheet = workbook[pmu]
    # Encontrando a célula "DE1F0" e obtendo sua posição
    de1f0_cell = find_cell_value(worksheet, "DE1F0", 9)
    if de1f0_cell is not None:
        de1f0_col = de1f0_cell.column
        de1f0_row = de1f0_cell.row
        # Obtendo os valores nas colunas adjacentes
        freq_DE1F0 = worksheet.cell(row=de1f0_row, column=de1f0_col + 1).value
        periodo_medio_DE1F0 = worksheet.cell(row=de1f0_row, column=de1f0_col + 2).value
        periodo_total_DE1F0 = worksheet.cell(row=de1f0_row, column=de1f0_col + 3).value
    else:
        freq_DE1F0 = 0
        periodo_medio_DE1F0 = 0
        periodo_total_DE1F0 = 0
    
    # Encontrando a célula "DE040" e obtendo sua posição
    de040_cell = find_cell_value(worksheet, "DE040", 9)
    if de040_cell is not None:
        de040_col = de040_cell.column
        de040_row = de040_cell.row
        # Obtendo os valores nas colunas adjacentes
        freq_DE040 = worksheet.cell(row=de040_row, column=de040_col + 1).value
        periodo_medio_DE040 = worksheet.cell(row=de040_row, column=de040_col + 2).value
        periodo_total_DE040 = worksheet.cell(row=de040_row, column=de040_col + 3).value
    else:
        freq_DE040 = 0
        periodo_medio_DE040 = 0
        periodo_total_DE040 = 0

    
    # Encontrando a célula "DE000" e obtendo sua posição
    de000_cell = find_cell_value(worksheet, "DE000", 9)
    if de000_cell is not None:
        de000_col = de000_cell.column
        de000_row = de000_cell.row
        # Obtendo os valores nas colunas adjacentes
        freq_DE000 = worksheet.cell(row=de000_row, column=de000_col + 1).value
        periodo_medio_DE000 = worksheet.cell(row=de000_row, column=de000_col + 2).value
        periodo_total_DE000 = worksheet.cell(row=de000_row, column=de000_col + 3).value
    else:
        freq_DE000 = 0
        periodo_medio_DE000 = 0
        periodo_total_DE000 = 0

    status_flags_diferente = 0
    column = worksheet['I']
    # Verificar se há valores diferentes de "DE1F0", "DE040" e "DE000" na coluna
    for cell in column:
        if cell.value and cell.value not in ['DE1F0', 'DE040', 'DE000','Status Flag']:
            status_flags_diferente = cell.value            
            break
    
    status_flags_diferente_cell = find_cell_value(worksheet, status_flags_diferente, 9)
    if  status_flags_diferente_cell is not None:
         status_flags_diferente_col = status_flags_diferente_cell.column
         status_flags_diferente_row = status_flags_diferente_cell.row
        # Obtendo os valores nas colunas adjacentes
         freq_status_flags_diferente = worksheet.cell(row=status_flags_diferente_row, column=status_flags_diferente_col + 1).value
         periodo_medio_status_flags_diferente = worksheet.cell(row=status_flags_diferente_row, column=status_flags_diferente_col + 2).value
         periodo_total_status_flags_diferente = worksheet.cell(row=status_flags_diferente_row, column=status_flags_diferente_col + 3).value
    else:
        freq_status_flags_diferente = 0
        periodo_medio_status_flags_diferente = 0
        periodo_total_status_flags_diferente = 0
     
    workbook.save(file_name)

    
    worksheet1 = workbook['Síntese']
    worksheet_exists = 'Síntese' in workbook.sheetnames
    
    if  worksheet_exists:         

        identificação = find_cell_value(worksheet1, pmu, 3)    
        identificação_col = identificação.column
        identificação_row = identificação.row       
        worksheet1.cell(row=identificação_row, column=identificação_col + 1).value = freq_DE1F0
        worksheet1.cell(row=identificação_row, column=identificação_col + 2).value = periodo_medio_DE1F0 
        worksheet1.cell(row=identificação_row, column=identificação_col + 3).value = periodo_total_DE1F0
        worksheet1.cell(row=identificação_row, column=identificação_col + 4).value = freq_DE040
        worksheet1.cell(row=identificação_row, column=identificação_col + 5).value = periodo_medio_DE040
        worksheet1.cell(row=identificação_row, column=identificação_col + 6).value = periodo_total_DE040
        worksheet1.cell(row=identificação_row, column=identificação_col + 7).value = freq_DE000
        worksheet1.cell(row=identificação_row, column=identificação_col + 8).value = periodo_medio_DE000
        worksheet1.cell(row=identificação_row, column=identificação_col + 9).value = periodo_total_DE000 
        worksheet1.cell(row=identificação_row, column=identificação_col + 10).value = freq_status_flags_diferente
        worksheet1.cell(row=identificação_row, column=identificação_col + 11).value = periodo_medio_status_flags_diferente
        worksheet1.cell(row=identificação_row, column=identificação_col + 12).value = periodo_total_status_flags_diferente  
    
    
    workbook.save(file_name)