def convert_decimal_to_binary(status_flags, item):
    binary_status_flags = bin(status_flags[item]['Value'])[2:]
    binary_status_flags = "0" * (8 - len(binary_status_flags) % 8) + binary_status_flags
    binary_list = [binary_status_flags[item:item+4]
                    for i in range(0, len(binary_status_flags), 4)]
    return " ".join(binary_list)