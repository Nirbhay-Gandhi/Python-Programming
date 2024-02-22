from queue import PriorityQueue

# Helper function to swap elements at indices i and j in a list
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

# Helper function to check if a state is the goal state
def is_goal(state):
    return state == sorted(state)

#print the list in the string format
def print_state(state): #[1,2,3,4]
    temp = list(map(str, state)) #['1','2','3','4']
    str_joined = ','.join(temp) 
    print(str_joined) 

def list_to_str(state): #[1,2,3,4]
    temp = list(map(str, state)) #['1','2','3','4']
    str_joined = ','.join(temp) 
    return str_joined 

# Heuristic function for Greedy and A* search (approximation)
def heuristic(state):
    return sum(abs(state[i] - state[i+1]) for i in range(len(state) - 1))

def cumm_heuristic(state):
    return heuristic(state)

def best_state(neighbours):
    heuristics = list(map(cumm_heuristic,neighbours))
    min_index = heuristics.index(min(heuristics)) 
    return neighbours[min_index]

"""
proceed ahed with the best heuristic only
"""

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

        # best_neighbor = min(neighbors, key=heuristic)
        best_neighbor = best_state(neighbors)
        #we can proceed ahed only, if the state is better than the current state
        if heuristic(best_neighbor) >= heuristic(current_state):
            break 
        current_state = best_neighbor

# Main function to parse input and call search algorithms
def main():
    input_str = input().strip()  # Read the input string
    numbers = input_str.split()  # Split the input string by spaces
    initial_state = [float(num) for num in numbers]  # Convert the numbers to floats

    hill_climbing(initial_state)


if __name__ == "__main__":
    main()