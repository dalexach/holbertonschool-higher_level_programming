#!/usr/bin/python3
"""
Function Pascal triangle
"""


def pascal_triangle(n):
    """
    Fucntion that returns a list of lists of intefers representating the
    Pascal's triangle of 'n'
    Attributes:
    @n: n Pascal's triangle
    Return:
    empty list if n <=0, otherwise the list with the representation
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    plist = [[1], [1, 1]]
    nlist = []
    aux = 0
    for i in range(2, n):
        while aux <= i:
            if aux - 1 < 0:
                nlist.append(1)
            elif aux == i:
                nlist.append(1)
            else:
                nlist.append(plist[i - 1][aux - 1] + plist[i - 1][aux])
            aux += 1
        plist.append(nlist)
        nlist = nlist[:]
        nlist.clear()
        aux = 0
    return plist
