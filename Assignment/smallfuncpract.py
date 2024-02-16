from queue import PriorityQueue

# Helper function to swap elements at indices i and j in a list
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

# Helper function to check if a state is the goal state
def is_goal(state):
    return state == sorted(state)

# Helper function to print the state
def print_state(state):
    print(','.join(map(str, state)))

# BFS (Breadth-First Search)
def bfs(initial_state):
    visited = set()
    queue = [initial_state]
    
    while queue:
        state = queue.pop(0)
        print_state(state)
        
        if is_goal(state):
            return
        
        visited.add(tuple(state))
        for i in range(len(state) - 1):
            next_state = state[:]
            swap(next_state, i, i + 1)
            if tuple(next_state) not in visited:
                queue.append(next_state)


# Main function to parse input and call search algorithms
def main():
    input_str = input().strip()  # Read the input string
    numbers = input_str.split()  # Split the input string by spaces
    initial_state = [float(num) for num in numbers]  # Convert the numbers to floats
    print("BFS:")
    bfs(initial_state)


if __name__ == "__main__":
    main()