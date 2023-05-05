import os
import shutil


def create_excel_file(date, server_name):
    parts = date.split("-")
    # Extract the day and month values from the parts list
    year = parts[2]
    month = parts[0]
    # Rename the destination file
    new_name = f"{year}_{month}_medfasee_{server_name}_status_flags.xlsx"
    new_path = os.path.join("./data/", new_name)

    if not os.path.exists(new_path):
        # Define the source and destination paths
        src_path = "./data/model.xlsx"
        dst_path = new_path

        # Copy the file from the source path to the destination path
        shutil.copy(src_path, dst_path)
        os.rename(dst_path, new_path)
