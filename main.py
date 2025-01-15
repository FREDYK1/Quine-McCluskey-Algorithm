
def decimal_to_binary(number, num_vars):
    # Convert decimal number to binary
    binary =bin(number)[2:].zfill(num_vars)
    return binary

def count_ones(binary):
    number = binary.count('1')
    return number

def group_minterms(minterms, num_vars):
    # Group minterms by number of ones
    groups = {}
    for minterm in minterms:
        binary = decimal_to_binary(minterm, num_vars)
        ones_count = count_ones(binary)
        if ones_count not in groups:
            groups[ones_count] =[]
        groups[ones_count].append(binary)
    return groups



# minterms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# # num_vars = 4
# # result = quine_mccluskey(minterms, num_vars)
# # print(result)