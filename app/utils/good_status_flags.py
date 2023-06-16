DATA_ERROR = 557056
TIME_QUALITY_SYNC = 64
PMU_ERROR = 909312

def good_status_flags(status):
    return (status == TIME_QUALITY_SYNC or status == DATA_ERROR or status == PMU_ERROR or status == 0)
