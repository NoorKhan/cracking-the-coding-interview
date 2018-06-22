# O(min(a, b)) 
def is_one_away(string_a, string_b):
    if abs(len(string_a) - len(string_b)) > 1:
        return False

    differences = 0
    if len(string_a) >= len(string_b):
        for i in range(0, len(string_b)):
            if string_b[i] != string_a[i]:
                differences += 1
                string_a = string_a[:i] + string_a[i + 1:]
            
            if differences > 1:
                return False
    else:
        for i in range(0, len(string_a)):
            if string_a[i] != string_b[i]:
                differences += 1
                string_b = string_b[:i] + string_b[i + 1:]
            
            if differences > 1:
                return False

    return True

print(is_one_away("abcc", "dabccd"))