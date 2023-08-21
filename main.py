from app.ppa_status_flags import ppa_status_flags
from app.get_bad_status_flags import GetBadStatusFlags

def main():
    server_name = "ons_pdcmi_bsb"
    port = ppa_status_flags[server_name]['port']
    date = '08-15-23'
    start_time = "00:00:00.000"
    end_time = "23:59:59.999"
    process_status_flags = GetBadStatusFlags(server_name, port, date, start_time, end_time)
    process_status_flags.execute()
main() 