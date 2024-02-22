from HelperFunctions import HelperFunc as Hf
from queue import PriorityQueue

class InformedSearchMethods:
    def Breadth_first_search(initial_state):
        print("Breadth First Search")
        visited = set()
        queue = []

        queue.append(initial_state)
        visited.add(Hf.list_to_str(initial_state))
    
        iteration = 0
        while queue:
            #pop the queue element 
            curr_state = queue.pop(0)
            print(f"[{iteration}]: {curr_state}")
        
            if Hf.is_goalstate(curr_state):
                return
        
            for i in range(len(curr_state) - 1):
                next_state = curr_state[:]
                Hf.swap(next_state, i, i + 1)
                if Hf.list_to_str(next_state) not in visited:
                    #visit the unvisited neighbours & put them into the queue
                    visited.add(Hf.list_to_str(next_state))
                    queue.append(next_state)
            iteration +=1
        return iteration


    def Depth_first_search(initial_state):
        print("Depth First Search")
        visited = set()
        stack = []

        stack.append(initial_state)
        visited.add(Hf.list_to_str(initial_state))

        iteration = 0
        while stack:
            #pop the queue element 
            curr_state = stack.pop()
            print(f"[{iteration}]: {curr_state}")
        
            if Hf.is_goalstate(curr_state):
                return
        
            for i in range(len(curr_state) - 1):
                next_state = curr_state[:]
                Hf.swap(next_state, i, i + 1)
                if Hf.list_to_str(next_state) not in visited:
                    #visit the unvisited neighbours & put them into the queue
                    visited.add(Hf.list_to_str(next_state))
                    stack.append(next_state)
            iteration +=1
        return iteration


    """
    - uniform cost search me hum goal state par reach karne ke liye hamesha wahi path use karte hai,
    jiska path cost sabse jyda kam hota hai
    - blindly jo action hume immediate min cost deta hai, hum usko choose karte hai

    -> how we'll find the optimal cost path? 
    we attch a priority with every state. that priority will act as a action cost required from one state to 
    next state
    """
    def Uniform_cost_search(initial_state):
        print("Uniform Cost Search")
        visited = set()
        priority_queue = PriorityQueue()
    
        priority_queue.put((0, initial_state))
        visited.add(Hf.list_to_str(initial_state))

        total_cost = 0
        iteration = 0
        while priority_queue:
            opern_cost, curr_state = priority_queue.get()
            print(f"[{iteration}]: Cost {opern_cost}  {curr_state}")
        
            if Hf.is_goalstate(curr_state):
                return
        
            #exploring out successors steps
            for i in range(len(curr_state) - 1):
                next_state = curr_state[:]
                Hf.swap(next_state, i, i + 1)
                if Hf.list_to_str(next_state) not in visited:
                    total_cost += 1  #Cost: 1 unit per action (given)
                    #visit the unvisited neighbours & put them into the queue
                    visited.add(Hf.list_to_str(next_state))
                    priority_queue.put((opern_cost+1, next_state))
            iteration+=1
        return iteration


class UnInformedSearchMethods:
    def Greedy_best_first_search(initial_state):
        print("Greedy Best First Search")
        visited = set()
        priority_queue = PriorityQueue()
    
        priority_queue.put((Hf.heuristic(initial_state), initial_state))
        visited.add(Hf.list_to_str(initial_state))

        iteration = 0
        while priority_queue:
            heurstc, curr_state = priority_queue.get()
            print(f"[{iteration}]: {curr_state}")
        
            if Hf.is_goalstate(curr_state):
                return
        
            for i in range(len(curr_state) - 1):
                next_state = curr_state[:]
                Hf.swap(next_state, i, i + 1)
                if Hf.list_to_str(next_state) not in visited:
                    #visit the unvisited neighbours & put them into the queue
                    visited.add(Hf.list_to_str(next_state))
                    priority_queue.put((Hf.heuristic(next_state), next_state))    
            iteration+=1 
        return iteration


    """
    f(n) = h(n)+g(n) 
    g(n) = actual cost from start node to n
    h(n) = estimation cost from n to goal node 

    - here, every node will have 2 properties:
    (a) actual cost, which we will keep the priority over here
    (b) the heuristic value, that we'll calculate in every step

    - jo action hume min f(n) deta hai, hum usko expand karte hai
    """
    def A_star_search(initial_state):
        print("A star Search")
        visited = set()
        priority_queue = PriorityQueue()

        priority_queue.put((Hf.heuristic(initial_state), 0, initial_state))
        visited.add(Hf.list_to_str(initial_state))

        iteration = 0
        while not priority_queue.empty():
            heurstc, opern_cost, curr_state = priority_queue.get()
            print(f"[{iteration}]: Cost {opern_cost}  {curr_state}")
        
            if Hf.is_goalstate(curr_state):
                return
        
            for i in range(len(curr_state) - 1):
                next_state = curr_state[:]      
                Hf.swap(next_state, i, i + 1)
                if Hf.list_to_str(next_state) not in visited:
                    #visit the unvisited neighbours & put them into the queue
                    visited.add(Hf.list_to_str(next_state))
                    nextOpern = opern_cost + 1      
                    priority_queue.put((nextOpern+Hf.heuristic(next_state), nextOpern, next_state))
            iteration+=1


    """
    proceed ahed with the best heuristic only
    """
    # Hill-Climbing Search
    def Hill_climb_search(state):
        print("Hill Climb Search")
        iteration = 0
        while True:
            print(f"[{iteration}]: {state}")
            neighbors = []

            for i in range(len(state) - 1):
                next_state = state[:]
                Hf.swap(next_state, i, i + 1)
                neighbors.append(next_state)

            best_neighbor_state = Hf.min_heurstic_neighbour(neighbors)
            #we can proceed ahed only, if the state is better than the current state
            if Hf.heuristic(best_neighbor_state) >= Hf.heuristic(state):
                break 
            state = best_neighbor_state
            iteration +=1


def main():
    str_nums = input()  
    nums = str_nums.split()  
    start_state = [float(num) for num in nums] 
    print("Breadth First Search:")
    InformedSearchMethods.Breadth_first_search(start_state)
    print("Depth First Search:")
    InformedSearchMethods.Depth_first_search(start_state)
    print("Uniform First Search:")
    InformedSearchMethods.Uniform_cost_search(start_state)
    print("Greedy Best First Search:")
    UnInformedSearchMethods.Greedy_best_first_search(start_state)
    print("A* Search:")
    UnInformedSearchMethods.A_star_search(start_state)
    print("Hill Climb Search:")
    UnInformedSearchMethods.Hill_climb_search(start_state)


if __name__ == "__main__":
    main()