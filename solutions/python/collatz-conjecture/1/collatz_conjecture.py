def steps(number):

    count = 0

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        elif number % 2 > 0:
            number = number * 3 + 1
        count += 1

    return count


steps(12)
