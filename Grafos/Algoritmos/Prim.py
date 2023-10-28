from collections import deque

def prim(g:list, po:int= 0):
    # TODO
    pass

g= [
    [(2, 1), (3, 2)],
    [(2, 0), (3, 2), (1, 3)],
    [(3, 0), (3, 1), (4, 3)],
    [(1, 1), (4, 2), (5, 4)],
    [(5, 3)]
]


print(prim(g))
