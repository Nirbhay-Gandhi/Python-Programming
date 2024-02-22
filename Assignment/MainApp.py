from SearchingMethods import InformedSearchMethods as ISM
from SearchingMethods import UnInformedSearchMethods as USM
from HelperFunctions import HelperFunc as Hf

choice = 0
str_nums = input("Enter Array: ")  
nums = str_nums.split()  
start_state = [float(num) for num in nums]  
start_state = Hf.remove_duplicates(start_state)

while(choice != -1):
    print("Searching Methods")
    print("1. Breadth First Search:")
    print("2. Depth First Search:")
    print("3. Uniform First Search:")
    print("4. Greedy Best First Search:")
    print("5. A* Search:")
    print("6. Hill Climb Search:")
    print("7. All Algorithm Compairison")

    choice = int(input("Algorithm Choice:- "))
    
    match choice:
        case 1:
            USM.Breadth_first_search(start_state)
        case 2:
            USM.Depth_first_search(start_state)
        case 3:
            USM.Uniform_cost_search(start_state)
        case 4:
            ISM.Greedy_best_first_search(start_state)
        case 5:
            ISM.A_star_search(start_state)
        case 6:
            ISM.Hill_climb_search(start_state)
        case _:
            print("Invalid choice")

    choice = int(input("-1 to terminate, anyother key to continue: "))

             

    
    



