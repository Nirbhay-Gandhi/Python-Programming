# from queue import PriorityQueue

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def is_goalstate(lst):
    lst_sorted = sorted(lst)
    return lst == lst_sorted

def list_to_str(lst): 
    temp = list(map(str, lst)) 
    str_joined = ','.join(temp) 
    return str_joined 

def dfs(initial_state):
    visited = set()
    stack = []

    stack.append(initial_state)
    visited.add(list_to_str(initial_state))
    
    while stack:
        curr_state = stack.pop()
        print(list_to_str(curr_state))
        
        if is_goalstate(curr_state):
            return
        
        for i in range(len(curr_state) - 1):
            next_state = curr_state[:]
            swap(next_state, i, i + 1)
            if list_to_str(next_state) not in visited:
                stack.append(next_state)


def main():
    str_nums = input()  
    nums = str_nums.split()  
    start_state = [float(num) for num in nums] 
    print("DFS:")
    dfs(start_state)


if __name__ == "__main__":
    main()