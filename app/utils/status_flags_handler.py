PMU_ERROR = 909312
DATA_ERROR = 557056
TIME_QUALITY_SYNC = 64

def status_flags_handler(status):
    return (status == PMU_ERROR or status == DATA_ERROR or status == TIME_QUALITY_SYNC or status == 0)
