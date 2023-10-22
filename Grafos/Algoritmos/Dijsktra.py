from queue import PriorityQueue

def dijsktra_queue(g:list, po:int):
    # Definición de estructuras
    w= [float("inf")]*len(g) # Pesos
    s= [False]*len(g) # Visitados
    q= PriorityQueue() #Cola de prioridad: (peso, vértice)

    # Estado inicial de las estructuras
    w[po]= 0
    q.put((0, po))

    while not q.empty():
        v= q.get() # v= (peso, vértice)
        if s[v[1]]: continue # Si el vértice ya fue visitado continuamos con la siguiente iteración
        s[v[1]]= True # Marcar el vértice como visitado

        for e in g[v[1]]: # e= (vértice, peso)
            # Relajar el vértice
            lw= v[0]+ e[1] # Peso para llegar al vértice
            if w[e[0]]> lw: # Si el peso actual registrado es mayor al encontrado en la iteración
                w[e[0]]= lw # Reemplazar por el peso encontrado

                if not s[e[0]]: #Si el eje lleva a un vértice que no ha sido visitado
                    q.put( (w[e[0]], e[0]) ) # Añadir el vértice a la cola
    return w

g= [ [(4, 1), (2, 2)],
     [(3, 2), (2,3), (3, 4)],
     [(1, 1), (4, 3), (5, 4)],
     [],
     [(1, 3)]
]
#Expected Result: [0, 3, 2, 5, 6]
print(dijsktra(g, 0, 4))
