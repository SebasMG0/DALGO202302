from sys import stdin, stdout
from collections import deque

def fordFulk(f:list):
    pass

# f: Grafo, i:Inicial, e:Final
def bfs(f:list, i:int, e:int):
    q= deque([i])

    while q:
        n= q.popleft()

        for k in f[n]:



if __name__== "__main__":
    N= int( stdin.readline().strip() )
    E= int( stdin.readline().strip() )

    f= [[float("inf")]*N for _ in range(N)]

    for _ in range (N):
        line= stdin.readline().split()
        f[int(line[0])][int(line[1])]= int(line[2])
        f[int(line[1])][int(line[0])]= 0
    # fordFulk(f)



# BFS use FIFO
