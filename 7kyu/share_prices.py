def share_price(invested, changes):
    # oneliner
    # return invested if changes == [] else invested+sum(changes)
    if changes == []:
        return str(invested)+".00"
    for change in changes:
        invested *= 1+(change/100)
        round(invested, 2)
    breturn invested


print(share_price(100, [50, -50]))
