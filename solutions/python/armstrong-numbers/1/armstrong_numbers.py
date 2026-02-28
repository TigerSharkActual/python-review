def is_armstrong_number(number):

    digit = [int(digit) for digit in str(number)]
    power = len(digit)
    total = sum(digit ** power for digit in digit)

    if number == total:
        return True
    return False


is_armstrong_number(9)