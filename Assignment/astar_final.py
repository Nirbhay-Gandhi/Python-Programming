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

def heuristic(state):
    sorted_sate = state[:]
    sorted_sate.sort()
    heuristic_sum = 0 
    for element in state:
        heuristic_sum = heuristic_sum + abs(sorted_sate.index(element) - state.index(element))
    return heuristic_sum

# A* Search
"""
f(n) = h(n)+g(n) 
g(n) = actual cost from start node to n
h(n) = estimation cost from n to goal node 

- here, every node will have 2 properties:
(a) actual cost, which we will keep the priority over here
(b) the heuristic value, that we'll calculate in every step

- jo action hume min f(n) deta hai, hum usko expand karte hai
"""
def a_star(initial_state):
    visited = set()
    priority_queue = PriorityQueue()

    priority_queue.put((heuristic(initial_state), 0, initial_state))
    visited.add(list_to_str(initial_state))

    while not priority_queue.empty():
        heurstc, opern_cost, curr_state = priority_queue.get()
        print(curr_state)
        
        if is_goalstate(curr_state):
            return
        
        for i in range(len(curr_state) - 1):
            next_state = curr_state[:]      
            swap(next_state, i, i + 1)
            if list_to_str(next_state) not in visited:
                #visit the unvisited neighbours & put them into the queue
                visited.add(list_to_str(next_state))
                nextOpern = opern_cost + 1      
                priority_queue.put((nextOpern+heuristic(next_state), nextOpern, next_state))

def main():
    str_nums = input()  
    nums = str_nums.split()  
    start_state = [float(num) for num in nums] 
    print("UCS:")
    a_star(start_state)


if __name__ == "__main__":
    main()