def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2


"""
For testing purpose, we write some test functions
"""
print("name in mymath: ",__name__)
if __name__ == "__main__":
    print(f"testing addition method: {add(3,5)}")
    print(f"testing addition method: {add(-1,0)}")
    print(f"testing subtract method: {sub(3,5)}")