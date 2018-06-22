def print_permutation(string, current_permutation, length):
    if len(current_permutation) == length:
        print(current_permutation)

    for i in range(0, len(string)):
        splice = string[:i] + string[i + 1:]
        print_permutation(splice, current_permutation + string[i], length)
         
#print_permutation("abcd", "", 4)


# returns a list of all s! permuations of a given string were s is the length of the string
def get_permutations(string, current_permutation, length, permutations):
    if len(current_permutation) == length:
        permutations.append(current_permutation)

    for i in range(0, len(string)):
        splice = string[:i] + string[i + 1:]
        get_permutations(splice, current_permutation + string[i], length, permutations)

string = "abcd"
permutations = []
get_permutations(string, "", len(string), permutations)
print(permutations)