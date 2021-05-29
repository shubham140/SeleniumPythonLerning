def index_filter(indexes, string):
    str1=""
    for i in indexes:
        str1+=string[i]

    return str1.lower()



print(index_filter([2, 3, 8, 11], "Autumn in New York"))
