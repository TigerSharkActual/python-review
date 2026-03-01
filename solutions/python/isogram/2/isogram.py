def is_isogram(string):

    string_edit = [i for i in string.lower() if i.isalpha()]
    
    return len(set(string_edit)) == len(string_edit)


is_isogram("isogram")
