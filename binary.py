#converts a number to binary

def to_binary(n):
    s = ""
    
    def get_highest_power_of_two(n):
        count = 0

        while n > 1:
            n = n // 2
            count += 1
            
        return 2 ** count

    highest_power_of_two = get_highest_power_of_two(n)

    remainder = n - highest_power_of_two

    if remainder >= 0:
        s += "1"

        while True:
            highest_power_of_two = highest_power_of_two // 2

            if highest_power_of_two == 0:
                break
                
            if remainder >= highest_power_of_two:
                s += "1"

                remainder = remainder - highest_power_of_two
            else:
                s += "0"
    else:
        s += "0"

    return s

for i in range (0, 100):
    print(str(i) + ": " + to_binary(i))

def cheating_to_binary(n):
    powers_of_two = [128, 64, 32, 16, 8, 4, 2, 1]

    s = ""
    for i in powers_of_two:
        if n >= i:
            n = n - i
            s += "1"
        else:
            s += "0"
    
    return s

# for i in range(0, 100):
#     print(str(i) + ": " + cheating_to_binary(i), end="\n")