def convert_decimal_to_binary(status_flags):
    binary_status_flags = bin(status_flags[0]['Value']).zfill(20)[2:]
    return ' '.join(binary_status_flags[i:i+4] for i in range(0, len(binary_status_flags), 4))