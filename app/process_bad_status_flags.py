from .status_flags_handler import status_flags_handler

class StatusFlags:
    def process_bad_status_flags(self, data):
        status_flags = []
        previous_status_flag = None
        previous_good_status_flag = True
        for item in data['TimeSeriesDataPoints']:
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
        if not previous_good_status_flag:
            status_flags.append(item)
        return status_flags
