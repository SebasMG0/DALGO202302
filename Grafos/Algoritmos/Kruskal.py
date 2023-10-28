def kruskal(g:list, po:int):
    f= [{i} for i in range (len(g))] # Forest o conjunto de árboles -> En principio un arbol por cada vértice
    t= []
    q= []

    for i in range (len(g)):
        f.append({i})
        for j in range(len(g[i])):
            q.append((i, g[i][j][0], g[i][j][1]))

    q.sort(key= lambda edge: edge[2]) # Ejes ordenados por pesos: a, b, peso

    for i in range(len(q)):
        s= findSetIndex(f, q[i][0], q[i][1]) # s: índice_conjunto(a), índice_conjunto(b)
        if s[0]!= s[1]:
            t.append(q[i])
            joinSets(f, s[0], s[1])
    return t if len(t)==len(g)-1 else False

def findSetIndex(f:list, po:int, pf:int):
    o, l= -1, -1
    for i in range(len(f)):
        if po in f[i]:
            o= i
        if pf in f[i]:
            l= i
        if o>=0 and l>=0:
            break
    return o, l

def joinSets(f:list, s0, s1):
    f[s0]= f[s0] | f[s1]
    f[s1].clear()

# Nota: Para grafos no dirigidos
g1= [ [(1, 4), (2, 2)],
     [(2, 3), (3, 2), (4, 3)],
     [(1, 1), (3, 4), (4, 5)],
     [(4, 2)],
     [(3, 1)] ]
print(kruskal(g1, 0))
# MST hallado: [(2, 1, 1), (4, 3, 1), (0, 2, 2), (1, 3, 2), (3, 5, 2)]

g2= [
    [(1, 2), (3, 5)],
    [(2, 4), (3, 5)],
    [(5, 2)],
    [(4, 3)],
    [(5, 4)],
    []
]
print(kruskal(g2, 0))
# MST hallado: [(0, 1, 2), (2, 5, 2), (3, 4, 3), (1, 2, 4), (4, 5, 4)]
