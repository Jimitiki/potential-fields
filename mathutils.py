import math

def normalize(x, y):
    m = magnitude(x, y)
    return (x / m, y / m)

def magnitude(x, y):
    return math.sqrt(x * x + y * y)

def dot_product(u, v):
    return u[0] * v[0] + u[1] * v[1]
