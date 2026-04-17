import sys

# Define the goal state (common goal is 1-8, with 0 as the blank)
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)
N = 3

def solve_dfs(initial_state):
    """Solves the 8-puzzle problem using Depth-First Search."""
    stack = [(initial_state, [])] # (current_state, path_so_far)
    visited = set()
    visited.add(initial_state)

    while stack:
        current_state, path = stack.pop() # LIFO behavior for DFS

        if current_state == GOAL_STATE:
            return path # Goal reached, return the sequence of moves

        # Generate neighbors (possible moves)
        for move, neighbor_state in get_neighbors(current_state):
            if neighbor_state not in visited:
                visited.add(neighbor_state)
                new_path = path + [move]
                stack.append((neighbor_state, new_path)) # Push to stack

    return None # No solution found

def get_neighbors(state):
    """Generates all valid neighboring states from the current state."""
    neighbors = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, N) # Convert index to row and column

    # Possible moves: (direction, row_change, col_change)
    directions = [('up', -1, 0), ('down', 1, 0), ('left', 0, -1), ('right', 0, 1)]

    for direction, dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        # Check if the new position is within the grid boundaries
        if 0 <= new_row < N and 0 <= new_col < N:
            new_zero_index = new_row * N + new_col
            new_state_list = list(state)
            # Swap the blank tile with the adjacent tile
            new_state_list[zero_index], new_state_list[new_zero_index] = \
                new_state_list[new_zero_index], new_state_list[zero_index]
            new_state = tuple(new_state_list)
            neighbors.append((direction, new_state))
            
    return neighbors

def print_solution(path):
    """Prints the steps of the solution path."""
    if path is None:
        print("No solution found or puzzle is unsolvable.")
    else:
        print(f"Solved in {len(path)} moves.")
        print("Steps:")
        for i, move in enumerate(path):
            print(f"Move {i+1}: {move}")

# Example Usage
if __name__ == "__main__":
    # Example initial state (ensure it is a solvable puzzle)
    # A solvable example: (1, 2, 3, 0, 4, 6, 7, 5, 8)
    # An unsolvable example would result in None being returned
    initial_board = (1, 2, 3, 4, 0, 5, 6, 7, 8) 
    
    print(f"Initial State: {initial_board}")
    print(f"Goal State: {GOAL_STATE}")
    
    solution_path = solve_dfs(initial_board)
    print_solution(solution_path)
