def is_square(n):
    if n < 0:
        return False
    return True if int(n**0.5)**2 == n else False


print(is_square(0))
print(is_square(-1))
print(is_square(4))
