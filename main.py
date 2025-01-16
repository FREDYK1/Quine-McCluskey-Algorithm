def decimal_to_binary(number, num_vars):
    return bin(number)[2:].zfill(num_vars)

def count_ones(binary):
    return binary.count('1')

def group_minterms(minterms, num_vars):
    groups = {}
    for minterm in minterms:
        binary = decimal_to_binary(minterm, num_vars)
        ones_count = count_ones(binary)
        if ones_count not in groups:
            groups[ones_count] = []
        groups[ones_count].append(binary)
    return groups

def combine_terms(term1, term2):
    combined = ""
    diff_count = 0
    for bit1, bit2 in zip(term1, term2):
        if bit1 != bit2:
            combined += '-'
            diff_count += 1
        else:
            combined += bit1
    return combined if diff_count == 1 else None

def find_prime_implicants(minterms, num_vars):
    groups = group_minterms(minterms, num_vars)
    prime_implicants = set()
    while groups:
        new_groups = {}
        used = set()
        for i in sorted(groups.keys()):
            if i + 1 in groups:
                for term1 in groups[i]:
                    for term2 in groups[i + 1]:
                        combined = combine_terms(term1, term2)
                        if combined:
                            used.add(term1)
                            used.add(term2)
                            ones_count = count_ones(combined)
                            if ones_count not in new_groups:
                                new_groups[ones_count] = []
                            new_groups[ones_count].append(combined)
        for group in groups.values():
            for term in group:
                if term not in used:
                    prime_implicants.add(term)
        groups = new_groups
    return prime_implicants

def get_essential_prime_implicants(prime_implicants, minterms):
    coverage = {minterm: [] for minterm in minterms}
    for implicant in prime_implicants:
        for minterm in minterms:
            binary = decimal_to_binary(minterm, len(implicant))
            if all(bit1 == bit2 or bit1 == '-' for bit1, bit2 in zip(implicant, binary)):
                coverage[minterm].append(implicant)

    essential_prime_implicants = set()
    for minterm, implicants in coverage.items():
        if len(implicants) == 1:
            essential_prime_implicants.add(implicants[0])

    return essential_prime_implicants

def quine_mccluskey(minterms, dont_cares, num_vars):
    all_terms = minterms + dont_cares
    prime_implicants = find_prime_implicants(all_terms, num_vars)
    essential_prime_implicants = get_essential_prime_implicants(prime_implicants, minterms)
    return essential_prime_implicants

def binary_to_sop(binary):
    variables = ['A', 'B', 'C', 'D']
    term = ''
    for i, bit in enumerate(binary):
        if bit == '1':
            term += variables[i]
        elif bit == '0':
            term += variables[i] + "'"
    return term

def minimized_sop(essential_prime_implicants):
    return ' + '.join(binary_to_sop(implicant) for implicant in essential_prime_implicants)

# Example usage
minterms = [0, 1, 2, 5, 6, 7, 8, 9, 10, 14]
dont_cares = [4, 15]
num_vars = 4
essential_prime_implicants = quine_mccluskey(minterms, dont_cares, num_vars)
sop = minimized_sop(essential_prime_implicants)
print("Essential Prime Implicants:", essential_prime_implicants)
print("Minimized SOP:", sop)