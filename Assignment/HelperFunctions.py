from queue import PriorityQueue

class HelperFunc:

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
    
    def cumm_heuristic(state):
        return HelperFunc.heuristic(state)

    def min_heurstic_neighbour(neighbours):
        heuristics = list(map(HelperFunc.cumm_heuristic,neighbours))
        min_index = heuristics.index(min(heuristics)) 
        return neighbours[min_index]