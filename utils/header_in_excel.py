def header_in_excel(worksheet, pmu):
    # Merge cells for the pmu variable in the first row
    worksheet.merge_cells(start_row=1, end_row=1, start_column=1, end_column=7)
    worksheet.cell(row=1, column=1, value=pmu)

    # Set the column titles in the second row
    worksheet.cell(row=2, column=1, value='Número')
    worksheet.cell(row=2, column=2, value='Data')
    worksheet.cell(row=2, column=3, value='Status Flags openPDC (hex)')
    worksheet.cell(row=2, column=4, value='Status Flags openPDC (binário)')
    worksheet.cell(row=2, column=5, value='Início (UTC)')
    worksheet.cell(row=2, column=6, value='Fim (UTC)')
    worksheet.cell(row=2, column=7, value='Período')
