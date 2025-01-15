
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

def combine_terms(term1, term2):
    # Combine two terms if only one bit is different
    combined = ""
    diff_count = 0
    for bit1, bit2 in zip(term1, term2):
        if bit1 != bit2:
            combined += '-'
            diff_count += 1
        else:
            combined += bit1
    # Return combined term if only one bit is different
    return combined if diff_count == 1 else None

def find_prime_implicants(minterms, num_vars):
    groups = group_minterms(minterms, num_vars)
    prime_implicants = set()
    # Combine terms in adjacent groups
    while groups:
        new_groups = {}
        used = set()
        for i in sorted(groups.keys()):
            if i+1 in groups:
                for term1 in groups[1]:
                    for term2 in groups[i+1]:
                        combined = combine_terms(term1, term2)
                        if combined:
                            used.add(term1)
                            used.add(term2)
                            ones_count = count_ones(combined)
                            if ones_count not in new_groups:
                                new_groups[ones_count] = []
                            new_groups[ones_count].append(combined)
        # Add unused terms to prime implicants
        for group in groups.values():
            for term in group:
                if term not in used:
                    prime_implicants.add(term)
        groups = new_groups
    return prime_implicants

# minterms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# # num_vars = 4
# # result = quine_mccluskey(minterms, num_vars)
# # print(result)