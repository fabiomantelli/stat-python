def elapsed_time(request_start_time, request_end_time):
    # Calculate the elapsed time in minutes and seconds
    elapsed_time_minutes = (request_end_time - request_start_time) // 60
    elapsed_time_seconds = (request_end_time - request_start_time) % 60

    # Print the elapsed time
    print(
        f"[Elapsed time] {int(elapsed_time_minutes)} minutes and {int(elapsed_time_seconds)} seconds \n")
