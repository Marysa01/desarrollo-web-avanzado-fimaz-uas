import heapq #permite manejar una cola de prioridad (elige el menor valor primero)

# Estado objetivo
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Movimientos posibles: arriba, abajo, izquierda, derecha
MOVES = {
    "UP": -3,
    "DOWN": 3,
    "LEFT": -1,
    "RIGHT": 1
}

def manhattan(state):                              #Calcula qué tan lejos está el estado actual del objetivo
    """Calcula la distancia de Manhattan"""
    distance = 0
    for i in range(9):                             #Recorre cada ficha del tablero
        if state[i] == 0:
            continue
        goal_pos = GOAL_STATE.index(state[i])
        x1, y1 = divmod(i, 3)                      #Convierte posiciones a coordenadas (fila, columna)
        x2, y2 = divmod(goal_pos, 3)              
        distance += abs(x1 - x2) + abs(y1 - y2)    # Suma la distancia entre posición actual y objetivo
    return distance

def get_neighbors(state):
    """Genera estados vecinos"""
    neighbors = []
    zero_index = state.index(0)

    for move, delta in MOVES.items():              # Intenta mover el 0 en todas las direcciones
        new_index = zero_index + delta

        # Validar movimientos
        if move == "LEFT" and zero_index % 3 == 0:
            continue
        if move == "RIGHT" and zero_index % 3 == 2:
            continue
        if 0 <= new_index < 9:
            new_state = list(state)                 # Intercambia posiciones para generar un nuevo estado
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(tuple(new_state))

    return neighbors

def greedy_search(start):
    """Búsqueda voraz"""
    visited = set()
    pq = []

    # (heurística, estado, camino)
    heapq.heappush(pq, (manhattan(start), start, []))    #Inserta el estado inicial con su heurística en la cola

    while pq:
        h, current, path = heapq.heappop(pq)             # Extrae el estado con menor heurística
        
        # Evita procesar estados repetidos
        if current in visited:
            continue

        visited.add(current)

        if current == GOAL_STATE:
            return path + [current]
        # Si llega al estado objetivo, devuelve la solución

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(pq, (manhattan(neighbor), neighbor, path + [current]))

    return None

def print_solution(solution):
    """Imprime la solución paso a paso"""
    if not solution:
        print("No se encontró solución")
        return

    for step, state in enumerate(solution):
        print(f"\nPaso {step}:")
        for i in range(0, 9, 3):
            print(state[i:i+3])

# 🔹 Estado inicial (puedes cambiarlo)
initial_state = (0, 2, 3,
                 1, 4, 6,
                 7, 5, 8)

solution = greedy_search(initial_state)
print_solution(solution)

# Ejecuta el algoritmo y muestra la solución