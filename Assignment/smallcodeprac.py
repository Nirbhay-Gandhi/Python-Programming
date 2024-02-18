from queue import PriorityQueue


initial_state = [4,-10,-5,-3]
# queue = [initial_state, -9] #queue of queue
queue = []
queue.append(initial_state)
print(queue)

#print the list in the string format
def print_state(state): #[1,2,3,4]
    temp = list(map(str, state)) #['1','2','3','4']
    str_joined = ','.join(temp) 
    print(str_joined) 

state = [1,2,3,4]
print_state(state)

l = [2,1,3,4]
for i in range(len(l)-1):
    print(f"i:{i}, i+1:{i+1}, (l[{i}]-l[{i+1}]): {l[i]-l[i+1]}")

def heuristic(state):
    print(f"state: {state}")
    sorted_sate = state[:]
    sorted_sate.sort()
    print(f"sorted_state: {sorted_sate}")
    heuristic_sum = 0 
    for element in state:
        # print(f"sorted_sate.index({sorted_sate[i]}) - state.index(state[i])") 
        heuristic_sum = heuristic_sum + abs(sorted_sate.index(element) - state.index(element))
        # print(heuristic_sum)
    return heuristic_sum

l = [12,17,14]#[12,13,14,10]
print(heuristic(l))