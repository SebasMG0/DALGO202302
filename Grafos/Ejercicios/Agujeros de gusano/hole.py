def floydWarshall(g:list, n):
    for m in range(len(g)):
        for i in range(len(g)):
            for f in range(len(g)):
                g[i][f]= min(g[i][f], g[i][m]+g[m][f])

    for i in range(n):
        if g[i][i]<0: return True
    return False

def toMatrix(l:list, n):
    g= [[float("inf")]*n for _ in range(n)]
    for e in l:
        g[e[0]][e[1]]= e[2]

    for i in range(n):
        g[i][i]= 0
    return g


c=[
 [2,2, [[0,1,-1],[1,0,0]]],
 [4,4,[[0, 1, 10],[1, 2, 20],[2, 3, 30],[3, 0, -60]]], # Sistemas estelares, agujeros de gusano, viajes
 [3,3,[[0,1,1000],[1,2,15],[2,1,-42]]],
 [6,10,[[3,0,119],[1,4,-267],[3,1,232],[5,0,-87],[3,2,466],[0,2,-172],[0,4,18],[1,5,537],[3,5,-307],[0,3,844]]]
]

for l in c:
    g= toMatrix(l[2], l[0])
    print(floydWarshall(g, l[0]))
