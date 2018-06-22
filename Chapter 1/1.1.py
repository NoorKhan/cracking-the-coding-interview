def is_unique(string):
    for i in reversed(range(0, len(string))):
        if i != string.find(string[i]):
            return False

    return True

print(is_unique("abcdef"))

def is_unique2(string):
    dictionary = {}

    for char in string:
        if char in dictionary:
            return False

        dictionary[char] = None

    return True

print(is_unique2("abcgdefg")) # false
print(is_unique2("abcdefg"))

# O(n^2)
def is_unique3(string):
    # O(n) where n is the length of the string
    for i in range(0, len(string)):
        # O(n - i) = O(n), n - i times?, O(n^2)
        for k in range(i + 1, len(string)):
            if string[i] == string[k]:
                return False

    return True

print(is_unique3("abcgdefg")) # false
print(is_unique3("abcdefg")) # true