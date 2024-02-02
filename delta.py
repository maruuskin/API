def find_delta(l_corner, up_corner):
    l_corner = l_corner.split()
    up_corner = up_corner.split()
    delta = str(max(abs(float(l_corner[0]) - float(up_corner[0])), abs(float(l_corner[1]) - float(up_corner[1]))) / 3)
    return delta