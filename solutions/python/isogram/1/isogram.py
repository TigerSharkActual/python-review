def is_isogram(string):

    string_edit = string.replace('-', '').replace(' ', '')
    
    string_set = set(string_edit.lower())

    if len(string_set) == len(string_edit):
        return True
    return False


is_isogram("isogram")
