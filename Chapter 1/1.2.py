def is_permutation(string_a, string_b):
    if len(string_a) != len(string_b):
        return False

    # sort strings and walk comparing each character, O(n log n)
    sorted_a = sorted(string_a)
    sorted_b = sorted(string_b)

    for i in range(0, len(sorted_a)):
        if sorted_a[i] != sorted_b[i]:
            return False

    return True

print(is_permutation("ea2bc", "bace2"))

