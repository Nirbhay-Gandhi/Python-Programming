


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
        print(current_state)
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