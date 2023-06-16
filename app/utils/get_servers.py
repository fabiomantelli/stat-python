from app.utils.ppa_status_flags import ppa_status_flags

def get_server(server_name):
    try:
        return ppa_status_flags[server_name]['ip']
    except KeyError:
        return None
    except TypeError:
        return None