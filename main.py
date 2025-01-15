
def decimal_to_binary(number, num_vars):
    # Convert decimal number to binary
    binary =bin(number)[2:].zfill(num_vars)
    return binary
