from queue import PriorityQueue


initial_state = [4,-10,-5,-3]
queue = [initial_state] #queue of queue
print(queue)

def print_state(state): #[1,2,3,4]
    temp = list(map(str, state)) #['1','2','3','4']
    str_joined = ','.join(temp) 
    print(str_joined)

state = [1,2,3,4]
print_state(state)
