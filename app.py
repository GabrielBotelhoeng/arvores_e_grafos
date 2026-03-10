import heapq


class Grafo:
    def __init__(self):
        # Dicionário que armazena os vértices e suas conexões
        # Exemplo: {"Entrada": [("Biblioteca", 50), ("Cantina", 30)]}
        self.vertices = {}

    def adicionar_local(self, nome):
        """Adiciona um novo local ao grafo"""
        if nome not in self.vertices:
            self.vertices[nome] = []

    def conectar_locais(self, origem, destino, distancia):
        """
        Cria uma conexão entre dois locais.
        Como o grafo é não direcionado,
        a conexão vale nos dois sentidos.
        """
        self.vertices[origem].append((destino, distancia))
        self.vertices[destino].append((origem, distancia))

    def menor_caminho(self, inicio, destino):
        """
        Implementação do algoritmo de Dijkstra
        para encontrar o menor caminho entre
        dois pontos do grafo.
        """

        # Inicializa todas as distâncias como infinito
        distancias = {local: float("inf") for local in self.vertices}
        distancias[inicio] = 0

        # Guarda o caminho percorrido
        anteriores = {local: None for local in self.vertices}

        # Fila de prioridade
        fila = [(0, inicio)]

        while fila:
            distancia_atual, local_atual = heapq.heappop(fila)

            # Se chegou ao destino, pode parar
            if local_atual == destino:
                break

            for vizinho, peso in self.vertices[local_atual]:
                nova_distancia = distancia_atual + peso

                # Atualiza apenas se encontrou um caminho menor
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    anteriores[vizinho] = local_atual
                    heapq.heappush(fila, (nova_distancia, vizinho))

        # Reconstruindo o caminho final
        caminho = []
        atual = destino

        while atual is not None:
            caminho.insert(0, atual)
            atual = anteriores[atual]

        # Se não houver caminho possível
        if distancias[destino] == float("inf"):
            return None, None

        return caminho, distancias[destino]


# =========================
# CRIAÇÃO DO SISTEMA
# =========================

grafo = Grafo()

# Lista de locais do campus
locais = [
    "Entrada",
    "Biblioteca",
    "Cantina",
    "Bloco A",
    "Bloco B",
    "Secretaria",
    "Laboratório"
]

# Adiciona os locais ao grafo
for local in locais:
    grafo.adicionar_local(local)

# Conexões entre os locais (origem, destino, distância em metros)
conexoes = [
    ("Entrada", "Biblioteca", 50),
    ("Entrada", "Cantina", 30),
    ("Cantina", "Bloco A", 20),
    ("Bloco A", "Bloco B", 25),
    ("Bloco B", "Laboratório", 40),
    ("Biblioteca", "Secretaria", 35),
    ("Secretaria", "Laboratório", 30)
]

# Conecta os locais
for origem, destino, distancia in conexoes:
    grafo.conectar_locais(origem, destino, distancia)


# =========================
# INTERAÇÃO COM O USUÁRIO
# =========================

print("=== Sistema de Rotas Internas ===")
print("\nLocais disponíveis:")

for local in locais:
    print("-", local)

inicio = input("\nDigite o ponto de partida: ")
destino = input("Digite o destino: ")

if inicio not in grafo.vertices or destino not in grafo.vertices:
    print("\nLocal inválido. Verifique os nomes digitados.")
else:
    caminho, distancia_total = grafo.menor_caminho(inicio, destino)

    if caminho is None:
        print("\nNão existe caminho entre os pontos informados.")
    else:
        print("\nMenor caminho encontrado:")
        print(" -> ".join(caminho))
        print("Distância total:", distancia_total, "metros")