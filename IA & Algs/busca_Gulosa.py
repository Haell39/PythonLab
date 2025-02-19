# Representação do mapa como um dicionário de conexões e distâncias
mapa = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 2, 'E': 4},
    'C': {'A': 3, 'D': 7},
    'D': {'B': 2, 'C': 7, 'E': 6, 'F': 3},
    'E': {'B': 4, 'D': 6, 'F': 5},
    'F': {'D': 3, 'E': 5}
}

# Distâncias em linha reta até o objetivo (a heurística)
# F vai ser o objetivo
heuristica = {
    'A': 9,
    'B': 6,
    'C': 8,
    'D': 3,
    'E': 2,
    'F': 0
}

# Algoritmo de busca Greedy

def busca_gulosa(mapa, heuristica, inicio, objetivo):
    # Conjunto de nós já visitados
    visitados = set()
    
    # Nó atual é o nó inicial
    atual = inicio
    
    # Caminho percorrido
    caminho = [atual]
    
    # Enquanto não chegamos ao objetivo
    while atual != objetivo:
        # Encontrar todos os vizinhos que ainda não foram visitados
        vizinhos = {nodo: distancia for nodo, distancia in mapa[atual].items() 
                   if nodo not in visitados}
        
        if not vizinhos:
            return "Não há caminho possível"
        
        # Escolher o vizinho com menor valor heurístico
        proximo = min(vizinhos.keys(), key=lambda x: heuristica[x])
        
        # Marcar o nó atual como visitado
        visitados.add(atual)
        
        # Atualizar o nó atual
        atual = proximo
        caminho.append(atual)
    
    return caminho

caminho_guloso = busca_gulosa(mapa, heuristica, 'A', 'F')
print("Caminho encontrado (busca gulosa):", caminho_guloso)
    