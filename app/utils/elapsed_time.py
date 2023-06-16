def elapsed_time(request_start_time, request_end_time):
    elapsed_time_in_minutes = (request_end_time - request_start_time) // 60
    elapsed_time_in_seconds = (request_end_time - request_start_time) % 60
    print(
        f"[Elapsed time] {int(elapsed_time_in_minutes)} minutes and {int(elapsed_time_in_seconds)} seconds \n")
