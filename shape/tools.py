import numpy as np


def normalize(v):
    return v / (np.linalg.norm(v))


def middle(p1, p2):
    return (p1 + p2) / 2


def project_circle(p, r):
    return normalize(p) * r


def get_normal(v):
    return normalize(np.array((-v[1], v[0])))


def get_eq(v, p):
    n = get_normal(v)
    c = n[0] * p[0] + n[1] * p[1]
    return n, c


def solve(v1, p1, v2, p2):
    l1, c1 = get_eq(v1, p1)
    l2, c2 = get_eq(v2, p2)

    m1 = np.matrix([l1, l2])
    m2 = np.matrix([[c1], [c2]])
    return np.array(np.linalg.solve(m1, m2)).ravel()


def reduce_op(acc, p2):
    p1, res_sum = acc
    return p2, res_sum + np.linalg.norm(p2 - p1)
