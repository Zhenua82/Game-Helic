from random import randint as rand

def randbool(r, mxr):
    t = rand(0, mxr)
    return (t <= r)

def randcell(h, w):
    tw = rand(0, w - 1)
    th = rand(0, h - 1)
    return (th, tw)

def randcell2(h, w):
    t = rand(0, 7)
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [1, 1], [1, -1], [-1, 1]]
    dx, dy = moves[t][0], moves[t][1]
    return (h + dy, w + dx)
