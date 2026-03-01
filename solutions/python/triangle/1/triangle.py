# a + b ≥ c

def equilateral(sides):
    
    a, b, c = sorted(sides)
    unquie_sides = len(set(sides))
    if c > a + b or a + b + c == 0:
        return False
    if unquie_sides == 1:
        return True
    return False


equilateral([0, 0, 0])


# a + c ≥ b


def isosceles(sides):
    a, b, c = sorted(sides)
    unquie_sides = len(set(sides))
    if c > a + b or a + b + c == 0:
        return False
    if unquie_sides == 2 or unquie_sides == 1:
        return True
    return False


isosceles([2, 3, 4])


# b + c ≥ a


def scalene(sides):
    
    a, b, c = sorted(sides)
    unquie_sides = len(set(sides))
    if c > a + b or a + b + c == 0:
        return False
    if unquie_sides == 3:
        return True
    return False


scalene([2, 3, 7])
