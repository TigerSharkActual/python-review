
def convert(num):

    while num % 3 == 0 or num % 5 == 0 or num % 7 == 0:

        results = ""

        if num % 3 == 0:
            results += "Pling"
        if num % 5 == 0:
            results += "Plang"
        if num % 7 == 0:
            results += "Plong"
        return results

    return str(num)


convert(3)