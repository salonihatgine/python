import sys

def main(L:list):
    if type(L) != int:
        raise TypeError("Type error ")

    if len(L) == 0:
        raise ValueError("Emty list")

    for x in L:
        if type(x) != int:
            raise TypeError("input object not integer")

    m = L[0]
    i = 1
    while i < len(L):
        if L[i] > m:
            m = L[i]
        i = i + 1
        return m

    L1 = []

    try:
        ret = find_max(m)
        print("ret", ret)
    except TypeError as (e)