DATA_ERROR = 557056
TIME_QUALITY_SYNC = 64
PMU_ERROR = 909312

def status_flags_handler(status):
    return (status == TIME_QUALITY_SYNC or status == DATA_ERROR or status == PMU_ERROR or status == 0)
