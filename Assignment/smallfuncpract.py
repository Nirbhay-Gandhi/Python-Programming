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
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic(initial_state), 0, initial_state))
    
    while not priority_queue.empty():
        _, opern_cost, state = priority_queue.get()
        print_state(state)
        
        if is_goal(state):
            return
        
        for i in range(len(state) - 1):
            next_state = state[:]      
            swap(next_state, i, i + 1)
            next_cost = opern_cost + 1      
            priority_queue.put((next_cost+heuristic(next_state), next_cost, next_state))

# Main function to parse input and call search algorithms
def main():
    input_str = input().strip()  # Read the input string
    numbers = input_str.split()  # Split the input string by spaces
    initial_state = [float(num) for num in numbers]  # Convert the numbers to floats

    a_star(initial_state)


if __name__ == "__main__":
    main()