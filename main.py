from app.utils.ppa_status_flags import ppa_status_flags
from app.utils.process_status_flags import ProcessStatusFlags

def main():
    server_name = "ons_pdcmi_rj"
    port = ppa_status_flags[server_name]['port']
    date = '06-02-23'
    start_time = "00:00:00.000"
    end_time = "00:00:01.999"
    process_status_flags = ProcessStatusFlags(server_name, port, date, start_time, end_time)
    process_status_flags.execute()
main()
