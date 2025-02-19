# Representação do mapa como um dicionário de conexões e distâncias
mapa = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 2, 'E': 4},
    'C': {'A': 3, 'D': 7},
    'D': {'B': 2, 'C': 7, 'E': 6, 'F': 3},
    'E': {'B': 4, 'D': 6, 'F': 5},
    'F': {'D': 3, 'E': 5}
}

# Distâncias em linha reta até o objetivo (nossa heurística)
# Assumindo que F é nosso objetivo
heuristica = {
    'A': 9,
    'B': 6,
    'C': 8,
    'D': 3,
    'E': 2,
    'F': 0
}


def busca_a_estrela(mapa, heuristica, inicio, objetivo):
    
    # Conjunto aberto (nós a serem avaliados)
    abertos = {inicio}
    # Conjunto fechado (nós já avaliados)
    fechados = set()
    
    # Custo para chegar a cada nó (inicializado com infinito para todos, exceto o inicial)
    g_score = {node: float('inf') for node in mapa.keys()}
    g_score[inicio] = 0
    
    # Custo estimado total para cada nó (g + h)
    f_score = {node: float('inf') for node in mapa.keys()}
    f_score[inicio] = heuristica[inicio]
    
    # Para reconstruir o caminho
    veio_de = {}
    
    while abertos:
        # Encontrar o nó com menor f_score
        atual = min(abertos, key=lambda x: f_score[x])
        
        # Se chegamos ao objetivo, reconstruímos o caminho
        if atual == objetivo:
            caminho = []
            while atual in veio_de:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.append(inicio)
            caminho.reverse()
            return caminho
        
        # Remover o nó atual do aberto e adicionar ao fechado
        abertos.remove(atual)
        fechados.add(atual)
        
        # Verificar todos os vizinhos
        for vizinho, distancia in mapa[atual].items():
            if vizinho in fechados:
                continue
            
            # Calcular nova distância passando pelo nó atual
            tentativa_g_score = g_score[atual] + distancia
            
            # Adicionar vizinho ao aberto se ainda não estiver lá
            if vizinho not in abertos:
                abertos.add(vizinho)
            # Se o novo caminho for pior, ignorar
            elif tentativa_g_score >= g_score[vizinho]:
                continue
            
            # Este é o melhor caminho até agora, então guardamos
            veio_de[vizinho] = atual
            g_score[vizinho] = tentativa_g_score
            f_score[vizinho] = g_score[vizinho] + heuristica[vizinho]
    
    # Se chegamos aqui, não encontramos caminho
    return "Não há caminho possível"


    # Teste:

caminho_a_estrela = busca_a_estrela(mapa, heuristica, 'A', 'F')
print("Caminho encontrado (A*):", caminho_a_estrela)