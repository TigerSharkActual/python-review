def is_valid(isbn):
    isbn_check = isbn.replace('-', '')
    if len(isbn_check) != 10:
        return False
    for i in range(len(isbn_check)-1):
        if isbn_check[i].isalpha():
            return False
    if isbn_check[-1].lower() != "x" and not isbn_check[-1].isdigit():
        return False
        
    isbn_result = 0
    count = 10
    

    if isbn_check[-1] == 'X' or isbn_check[-1] == 'x':
        isbn_result = isbn_result + 10
        isbn_check = isbn_check.lower()
        isbn_check = isbn_check.replace('x', '')

        while count > 1:
            for char in isbn_check:
                char_int = int(char)
                char_int = char_int * count
                count = count - 1
                isbn_result = isbn_result + char_int
        remainder = isbn_result % 11
        if remainder == 0:
            return True
        else:
            return False

    else:
        for char in isbn_check:
            char_int = int(char)
            char_int = char_int * count
            count = count - 1
            isbn_result = isbn_result + char_int
        remainder = isbn_result % 11
        if remainder == 0:
            return True
        else:
            return False


is_valid("3-598-21508-8")
