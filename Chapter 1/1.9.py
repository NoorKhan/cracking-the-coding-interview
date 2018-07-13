def is_rotated_substring(s1, s2):
    if len(s1) != len(s2):
        return False

    substring = ""

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            substring += s1[i]
        else:
            continue

    print(substring)
    return substring in s2

print(is_rotated_substring("abcd", "bcda"))