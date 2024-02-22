
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def is_goalstate(lst):
    lst_sorted = sorted(lst)
    return lst == lst_sorted

def list_to_str(lst): 
    temp = list(map(str, lst)) 
    str_joined = ','.join(temp) 
    return str_joined

def heuristic(state):
    sorted_sate = state[:]
    sorted_sate.sort()
    heuristic_sum = 0 
    for element in state:
        heuristic_sum = heuristic_sum + abs(sorted_sate.index(element) - state.index(element))
    return heuristic_sum


def cumm_heuristic(state):
    return heuristic(state)

def min_heurstic_neighbour(neighbours):
    heuristics = list(map(cumm_heuristic,neighbours))
    min_index = heuristics.index(min(heuristics)) 
    return neighbours[min_index]

"""
proceed ahed with the best heuristic only
"""

# Hill-Climbing Search
def hill_climbing(initial_state):
    curr_state = initial_state
    
    while True:
        print(curr_state)
        neighbors = []

        for i in range(len(curr_state) - 1):
            next_state = curr_state[:]
            swap(next_state, i, i + 1)
            neighbors.append(next_state)

        # best_neighbor = min(neighbors, key=heuristic)
        best_neighbor_state = min_heurstic_neighbour(neighbors)
        #we can proceed ahed only, if the state is better than the current state
        if heuristic(best_neighbor_state) >= heuristic(curr_state):
            break 
        curr_state = best_neighbor_state

def main():
    str_nums = input()  
    nums = str_nums.split()  
    start_state = [float(num) for num in nums] 
    # print("UCS:")
    hill_climbing(start_state)


if __name__ == "__main__":
    main()