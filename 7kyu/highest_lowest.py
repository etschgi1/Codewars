test = "1480 992 965 1203 1262 1994 1123 791 2589 1751 3024 2188 713 2117 2620 1471 27 -66 1470 1614 2836 66"


def high_and_low(numbers):
    n = list(map(int, numbers.split()))
    return ("{} {}".format(max(n), min(n)))


print(high_and_low(test))
