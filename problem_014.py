# 13 40 20 10 5 16 8 4 2 1
# 13
# 13 -> 3*13+1 = 40
# 40 -> 40/2 = 20
# 20 -> 20/2 = 10
# 10 -> 10/2 = 5
# 5 -> 3*5+1 = 16
# 16 -> 16/2 = 8
# 8 -> 8/2 = 4
# 4 -> 4/2 = 2
# 2 -> 2/2 = 1

def build_sequence(n, sequence):
    if n == 1:
        return sequence

    if sequence == []:
        sequence.append(n)

    if n % 2 == 0:
        n = n / 2
    else:
        n = 3*n+1

    sequence.append(n)
    return build_sequence(n, sequence)


def get_largest_sequence_number_in_sequences(sequences):
    longest_sequence = []
    for sequence in sequences:
        if len(sequence) > len(longest_sequence):
            longest_sequence = sequence
    return longest_sequence[0]

def get_all_sequences(n_range):
    list_of_sequences = []
    for n in n_range:
        list_of_sequences.append(build_sequence(n, []))
    return list_of_sequences

if __name__ == "__main__":
    n = get_largest_sequence_number_in_sequences(get_all_sequences(range(1, 1000000)))
    print(n) # 837799
