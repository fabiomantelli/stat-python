
DATA_ERROR = 557056
TIME_QUALITY_SYNC = 64


def good_status_flags(status):
    return (status == TIME_QUALITY_SYNC or status == DATA_ERROR or status == 0)
