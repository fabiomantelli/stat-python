def create_file_name(date, server_name):
    parts = date.split("-")
    year = parts[2]
    month = parts[0]
    file_name = f"./data/{year}_{month}_medfasee_{server_name}_status_flags.xlsx"
    return file_name