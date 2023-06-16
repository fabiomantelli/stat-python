from .status_flags_handler import status_flags_handler

def process_data(data_json):
    status_flags = []
    previous_status_flag = None
    previous_good_status_flag = True
    
    for i, item in enumerate(data_json['TimeSeriesDataPoints']):
        good_status_flag = status_flags_handler(item['Value'])
        
        if previous_good_status_flag and not good_status_flag:
            status_flags.append(item)
            previous_good_status_flag = False
        elif not previous_good_status_flag:
            if good_status_flag:
                status_flags.append(previous_status_flag)
                previous_good_status_flag = True
            elif item['Value'] != previous_status_flag['Value']:
                status_flags.append(previous_status_flag)
                status_flags.append(item)
        
        previous_status_flag = item
        
        if i == len(data_json['TimeSeriesDataPoints']) - 1:
            if not previous_good_status_flag:
                status_flags.append(item)
    
    return status_flags
