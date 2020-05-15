def make_readable(seconds):
    s = seconds % 60
    h = seconds//60//60
    m = seconds//60 - h*60
    return ("{:02}:{:02}:{:02}".format(h, m, s))


for i in range(0, 1000000, 5000):
    print(make_readable(i))
