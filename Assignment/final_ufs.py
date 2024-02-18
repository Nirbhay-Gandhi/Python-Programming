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

"""
- uniform cost search me hum goal state par reach karne ke liye hamesha wahi path use karte hai,
jiska path cost sabse jyda kam hota hai
- blindly jo action hume immediate min cost deta hai, hum usko choose karte hai

-> how we'll find the optimal cost path? 
we attch a priority with every state. that priority will act as a action cost required from one state to 
next state
"""
def ucs(initial_state):
    visited = set()
    priority_queue = PriorityQueue()
    
    priority_queue.put((0, initial_state))
    visited.add(list_to_str(initial_state))

    total_cost = 0
    iteration = 0
    while priority_queue:
        opern_cost, curr_state = priority_queue.get()
        print(f"[{iteration}]: Cost {opern_cost}  {curr_state}")
        
        if is_goalstate(curr_state):
            return
        
        #exploring out successors steps
        for i in range(len(curr_state) - 1):
            next_state = curr_state[:]
            swap(next_state, i, i + 1)
            if list_to_str(next_state) not in visited:
                total_cost += 1  #Cost: 1 unit per action (given)
                #visit the unvisited neighbours & put them into the queue
                visited.add(list_to_str(next_state))
                priority_queue.put((opern_cost+1, next_state))
        iteration+=1


def main():
    str_nums = input()  
    nums = str_nums.split()  
    start_state = [float(num) for num in nums] 
    print("UCS:")
    ucs(start_state)


if __name__ == "__main__":
    main()