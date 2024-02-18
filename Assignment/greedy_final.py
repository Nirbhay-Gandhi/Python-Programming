from queue import PriorityQueue

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def is_goalstate(lst):
    lst_sorted = sorted(lst)
    return lst == lst_sorted

def list_to_str(lst): 
    temp = list(map(str, lst)) 
    str_joined = ','.join(temp) 
    return str_joined

# Heuristic function for Greedy and A* search (approximation)
"""
Heuristic function calculated on the basis of the Manhatten Distance method:
means, it is the cummulative of how much distance each element has to travell inorder to reach
the correct place
"""
def heuristic(state):
    sorted_sate = state[:]
    sorted_sate.sort()
    heuristic_sum = 0 
    for element in state:
        heuristic_sum = heuristic_sum + abs(sorted_sate.index(element) - state.index(element))
    return heuristic_sum

# Greedy Search
def greedy(initial_state):
    visited = set()
    priority_queue = PriorityQueue()
    
    priority_queue.put((heuristic(initial_state), initial_state))
    visited.add(list_to_str(initial_state))

    while not priority_queue.empty():
        _, state = priority_queue.get()
        print(state)
        
        if is_goalstate(state):
            return
        
        for i in range(len(state) - 1):
            next_state = state[:]
            swap(next_state, i, i + 1)
            if list_to_str(next_state) not in visited:
                #visit the unvisited neighbours & put them into the queue
                visited.add(list_to_str(next_state))
                priority_queue.put((heuristic(next_state), next_state))


def main():
    str_nums = input()  
    nums = str_nums.split()  
    start_state = [float(num) for num in nums] 
    print("UCS:")
    greedy(start_state)


if __name__ == "__main__":
    main()