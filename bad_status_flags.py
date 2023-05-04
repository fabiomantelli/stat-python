
DATA_ERROR = 557056
TIME_QUALITY_SYNC = 64

def bad_status_flags(status):
    return not (status == TIME_QUALITY_SYNC or status == DATA_ERROR or status == 0)