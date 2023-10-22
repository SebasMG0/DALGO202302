def dfs(g:list):
    stack= [0]
    visited= []
    parents= []

    while stack:
        i= stack.pop(-1)
        if i in visited:
            return False
        
        visited.append(i)
        parents.append(i)
        for j in g[i]:
            if j not in parents:
                stack.append(j)
    return len(visited)==len(g)


def getGraph(g:str):
    # Función para convertir el string  del grafo en lista
    l= []
    for i in range(1, len(g)-2):
        c= g[i]
        if c=="[": l.append([])
        elif c.isdigit():l[-1].append(int(c))
    return l
       

if __name__== "__main__":
    from sys import stdin, stdout
    stdin.readline().strip()
    l= stdin.readline().strip()
    while len(l) > 0:
        stdout.write(str(dfs(getGraph(l)))+"\n")
        l= stdin.readline().strip()