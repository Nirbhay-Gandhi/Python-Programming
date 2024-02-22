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

# Heuristic function for Greedy and A* search (approximation)
def heuristic(state):
    return sum(abs(state[i] - state[i+1]) for i in range(len(state) - 1))

# BFS (Breadth-First Search)
def bfs2(initial_state):
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


# DFS (Depth-First Search)
def dfs(initial_state):
    visited = set()
    stack = [initial_state]
    
    while stack:
        state = stack.pop()
        print_state(state)
        
        if is_goal(state):
            return
        
        visited.add(tuple(state))
        for i in range(len(state) - 1):
            next_state = state[:]
            swap(next_state, i, i + 1)
            if tuple(next_state) not in visited:
                stack.append(next_state)

# UCS (Uniform Cost Search)
def ucs(initial_state):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, initial_state))
    
    while not priority_queue.empty():
        cost, state = priority_queue.get()
        print_state(state)
        
        if is_goal(state):
            return
        
        visited.add(tuple(state))
        for i in range(len(state) - 1):
            next_state = state[:]
            swap(next_state, i, i + 1)
            if tuple(next_state) not in visited:
                next_cost = cost + 1  # Cost of each action is 1 unit
                priority_queue.put((next_cost, next_state))

# Greedy Search
def greedy(initial_state):
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic(initial_state), initial_state))
    
    while not priority_queue.empty():
        _, state = priority_queue.get()
        print_state(state)
        
        if is_goal(state):
            return
        
        for i in range(len(state) - 1):
            next_state = state[:]
            swap(next_state, i, i + 1)
            priority_queue.put((heuristic(next_state), next_state))

# A* Search
def a_star(initial_state):
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic(initial_state), 0, initial_state))
    
    while not priority_queue.empty():
        _, cost, state = priority_queue.get()
        print_state(state)
        
        if is_goal(state):
            return
        
        for i in range(len(state) - 1):
            next_state = state[:]
            swap(next_state, i, i + 1)
            next_cost = cost + 1
            priority_queue.put((heuristic(next_state) + next_cost, next_cost, next_state))

# Hill-Climbing Search
def hill_climbing(initial_state):
    current_state = initial_state
    
    while True:
        print_state(current_state)
        neighbors = []
        for i in range(len(current_state) - 1):
            next_state = current_state[:]
            swap(next_state, i, i + 1)
            neighbors.append(next_state)
        best_neighbor = min(neighbors, key=heuristic)
        if heuristic(best_neighbor) >= heuristic(current_state):
            break
        current_state = best_neighbor

# Main function to parse input and call search algorithms
def main():
    # n, *numbers = input().split()
    # initial_state = [float(num) for num in numbers]
    # print("BFS:")
    # bfs(initial_state)

    input_str = input().strip()  # Read the input string
    numbers = input_str.split()  # Split the input string by spaces
    initial_state = [float(num) for num in numbers]  # Convert the numbers to floats
    print("BFS:")
    bfs(initial_state)

    # print("\nDFS:")
    # dfs(initial_state)

    # print("\nUCS:")
    # ucs(initial_state)
    
    # print("\nGreedy Search:")
    # greedy(initial_state)
    
    # print("\nA* Search:")
    # a_star(initial_state)
    
    # print("\nHill-Climbing Search:")
    # hill_climbing(initial_state)

if __name__ == "__main__":
    main()











def sayHi(num):
    print("hi ", num)
num = 4
match num:
    case 1:
        print("case 1")
        sayHi(1)
    case 2:
        print("case 2")
        sayHi(2)
    case 3:
        print("case 3")
        sayHi(3)
    case _:
        print("generic")
    