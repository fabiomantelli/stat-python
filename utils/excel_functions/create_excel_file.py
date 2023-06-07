import os
import shutil

def create_excel_file(date, server_name):
    month, day, year = date.split("-")
    excel_file_name = f"{year}_{month}_{server_name}_status_flags.xlsx"
    path = os.path.join("./data/", excel_file_name)

    if not os.path.exists(path):
        source_path = f"./data/model_{server_name}.xlsx"
        destination_path = path

        shutil.copy(source_path, destination_path)
        os.rename(destination_path, path)
