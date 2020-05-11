import itertools


def get_pins(observed):
    neighbours = {"1": ["1", "2", "4"],
                  "2": ["2", "1", "3", "5"],
                  "3": ["3", "2", "6"],
                  "4": ["4", "1", "5", "7"],
                  "5": ["5", "2", "4", "6", "8"],
                  "6": ["6", "3", "5", "9"],
                  "7": ["7", "4", "8"],
                  "8": ["5", "7", "8", "9", "0"],
                  "9": ["9", "6", "8"],
                  "0": ["0", "8"]}
    possible = []
    # get all possible for each num
    for num in observed:
        possible.append(neighbours[str(num)])
    # generate all possible codes from possible
    lists = []
    for lis in itertools.product(*possible):
        lists.append("".join(lis))
    return lists


testpin = "11"
print(get_pins(testpin))
