"""There once was a wise servant who saved the life of a prince.
The king promised to pay whatever the servant could dream up.
Knowing that the king loved chess, the servant told the king he would like to have grains of wheat.
One grain on the first square of a chessboard,
with the number of grains doubling on each successive square."""

def square(number):
    """This uses 2 ** (number - 1) to solve for how many grains of grain are on a particular square on the board."""

    grain_num = 2 ** (number - 1)

    if number in range(1, 65):
        return grain_num
    raise ValueError("square must be between 1 and 64")


square(64)


def total():
    """This is the total amount of grain on the board."""
    complete_grain_count = 1 * (2 ** 64 - 1)/(2 - 1)
    return int(complete_grain_count) - 1


total()
