from utils.good_status_flags import good_status_flags


def process_data(my_dict):
    status_flags = []
    flag = False

    for i, item in enumerate(my_dict['TimeSeriesDataPoints']):
        value = item['Value']
        filtered_value = good_status_flags(value)

        if (flag is False and filtered_value is False):
            status_flags.append(item)
            flag = True

            if i == len(my_dict['TimeSeriesDataPoints']) - 1:
                status_flags.append(item)
                return status_flags

        elif (flag is True and filtered_value is True):
            status_flags.append(current_status_flags)
            flag = False
        
        elif (flag is True and value != current_status_flags['Value']):
            status_flags.append(current_status_flags)
            status_flags.append(item)

            if i == len(my_dict['TimeSeriesDataPoints']) - 1:
                status_flags.append(item)
                return status_flags
        
        elif (flag is True and i == len(my_dict['TimeSeriesDataPoints']) - 1):
            status_flags.append(item)
        
        
        current_status_flags = item
    return status_flags
