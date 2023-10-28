def fwar(g:list):
    for initial in range(len(g)):
        for middle in range(len(g)):
            for out in range(len(g)):
                g[initial][out]= min(g[initial][out], g[initial][middle]+g[middle][out])
    return g
