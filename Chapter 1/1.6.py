# O(n)
def string_compression(string):
    compressed_string = string[0]

    count = 1
    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            count += 1
        else:
            compressed_string += str(count) + string[i]
            count = 1
    
    compressed_string += str(count)

    if len(compressed_string) < len(string):
        return compressed_string
    else:
        return string


print(string_compression("aabbbbcccccaaa"))
    