def most_frequent(string):
    dict1 = {}
    for char in string:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
    sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
    for char, freq in sorted_dict.items():
        print(char, freq)
most_frequent("mississippi")
