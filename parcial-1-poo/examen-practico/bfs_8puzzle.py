from collections import deque

def bfs(start_state):
    """
    Solves the 8-puzzle using BFS. Returns the path of states or None.
    """
    target = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    queue = deque([tuple(start_state)])
    visited = {tuple(start_state): None}

    while queue:
        current = queue.popleft()
        if current == target:
            path = []
            while current:
                path.append(list(current))
                current = visited[current]
            return path[::-1]

        zero_idx = current.index(0)
        row, col = divmod(zero_idx, 3)

        for move in (-3, 3, -1, 1):
            n_idx = zero_idx + move
            if 0 <= n_idx < 9 and abs(row - divmod(n_idx, 3)[0]) + abs(col - divmod(n_idx, 3)[1]) == 1:
                new_state = list(current)
                new_state[zero_idx], new_state[n_idx] = new_state[n_idx], new_state[zero_idx]
                new_state_tuple = tuple(new_state)

                if new_state_tuple not in visited:
                    visited[new_state_tuple] = current
                    queue.append(new_state_tuple)
    return None

initial = [1, 3, 0 , 6, 8, 4, 7, 5, 2]
solution = bfs(initial)
if solution:
    print(f"Path found in {len(solution)-1} moves.")
    for state in solution:
        print(f"{state[0:3]}\n{state[3:6]}\n{state[6:9]}\n-----")