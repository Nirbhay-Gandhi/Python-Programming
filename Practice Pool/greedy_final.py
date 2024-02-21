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

"""
f(n) = h(n)
- greedy best first search me hum goal state par reach karne ke liye hamesha wahi path use karte hai,
jiska heuristic sabse jyda kam hota hai
- blindly jo action hume immediate min heuristic deta hai, hum usko choose karte hai

-> how we'll find the optimal heuristic path? 
we attch a heuristic with every state. that heuristic will act as a action cost required from one state to 
next state
"""

# Greedy Search
def greedy(initial_state):
    visited = set()
    priority_queue = PriorityQueue()
    
    priority_queue.put((heuristic(initial_state), initial_state))
    visited.add(list_to_str(initial_state))

    while not priority_queue.empty():
        heurstc, curr_state = priority_queue.get()
        print(curr_state)
        
        if is_goalstate(curr_state):
            return
        
        for i in range(len(curr_state) - 1):
            next_state = curr_state[:]
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