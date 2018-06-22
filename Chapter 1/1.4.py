def is_palindrome_permutation(string):
    dictionary = {}
    
    for c in string.lower():
        if c != ' ':
            if c in dictionary:
                dictionary[c] += 1
            else:
                dictionary[c] = 1

    number_of_odd_characters = 0

    for k in dictionary.keys():
        if dictionary[k] % 2 == 1:
            number_of_odd_characters += 1

        if number_of_odd_characters > 1:
            return False

    return True

print(is_palindrome_permutation("Tact coa"))

    

    
