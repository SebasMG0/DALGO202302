from sys import stdin, stdout

# TODO:

if __name__ == "__main__":

    n= int(stdin.readline().strip()) # Nodos
    while n!= 0:
        m= int(stdin.readline().strip()) # Streets

        g= [[] for _ in range (n)] # Inicialización del grafo como una lista de adyacencia (Los nodos comienzan desde 0)
        q= []

        for i in range(m):
            l= stdin.readline().strip().split()

            edge= (int(l[1])-1, int(l[2]))
            g[int(l[0])-1].append(edge) # Se añaden las conexiones a la lista de adyacencia
            q.append((int(l[0])-1, int(l[1])-1, int(l[2]))) # Se crea una lista con los ejes
            
        # k= Algoritm
        stdout.write("\n")
        n= int(stdin.readline().strip()) # Nodos
