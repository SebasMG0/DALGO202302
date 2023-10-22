from collections import deque

def prim(g:list, po:int= 0):
    vi= [po]
    vw= [0]

    while len(vi)<len(g):
        m= (float("inf"), -1)
        for v in vi:
            mv= min(g[v], key= lambda x: x[0] if x[1] not in vi else float("inf"))
            if mv[0]<m[0]: m= mv

        vi.append(m[1])
        vw.append(m[0])
    return list(zip(vw, vi))

g= [
    [(2, 1), (3, 2)],
    [(2, 0), (3, 2), (1, 3)],  
    [(3, 0), (3, 1), (4, 3)],  
    [(1, 1), (4, 2), (5, 4)],
    [(5, 3)]
]


print( prim(g))
