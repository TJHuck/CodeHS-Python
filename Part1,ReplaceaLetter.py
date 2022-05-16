def replace_at_index(old, index):
    string = list(old)
    string[index] = "-";
    returnString = ""
    x = len(old)
    for i in range(x):
        returnString = returnString + string[i]
    return returnString
        
print(replace_at_index("eggplant", 3))
