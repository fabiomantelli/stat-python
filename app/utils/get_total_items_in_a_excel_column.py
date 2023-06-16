from collections import Counter

def get_total_items_in_an_excel_column(worksheet, column):
    status_flags = []
    count_total_status_flags = 0
    for row in worksheet.iter_rows(min_row=3, min_col=column, values_only=True):
        if row[0] is not None:
            status_flags.append(row[0])
            count_total_status_flags += 1
    counter = Counter(status_flags)
    most_common_status_flags, count = counter.most_common(1)[0]
    return most_common_status_flags, count_total_status_flags