from .good_status_flags import good_status_flags


def process_data(data_json):
    status_flags = []
    current_status_flags = None
    flag = False

    for i, item in enumerate(data_json['TimeSeriesDataPoints']):
        value = item['Value']
        filtered_value = good_status_flags(value)

        if (flag is False and filtered_value is False):
            status_flags.append(item)
            flag = True

            if i == len(data_json['TimeSeriesDataPoints']) - 1:
                status_flags.append(item)
                return status_flags

        elif (flag is True and filtered_value is True):
            status_flags.append(current_status_flags)
            flag = False

        elif (flag is True and value != current_status_flags['Value']):
            status_flags.append(current_status_flags)
            status_flags.append(item)

            if i == len(data_json['TimeSeriesDataPoints']) - 1:
                status_flags.append(item)
                return status_flags

        elif (flag is True and i == len(data_json['TimeSeriesDataPoints']) - 1):
            status_flags.append(item)

        current_status_flags = item

    return status_flags
