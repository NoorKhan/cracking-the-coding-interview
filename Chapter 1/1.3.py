def urlify(string):
    urlified_string = ""
    
    for c in string:
        if c == ' ':
            urlified_string += "%20"
        else:
            urlified_string += c

    return urlified_string

print(urlify("a b c "))