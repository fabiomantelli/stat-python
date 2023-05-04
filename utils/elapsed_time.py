def elapsed_time(start_time, end_time):
    # Calculate the elapsed time in minutes and seconds
    elapsed_time_minutes = (end_time - start_time) // 60
    elapsed_time_seconds = (end_time - start_time) % 60

    # Print the elapsed time
    print(
        f"[Elapsed time] {int(elapsed_time_minutes)} minutes and {int(elapsed_time_seconds)} seconds \n")
