class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert():
    head = None
    tail = None
    data = input()

    while int(data) != -1:
        newNode = Node(data)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next
        data = input()
    # print(f"head: {head.data}")
    return head

def print_list(head):
    curr = head
    while head != None:
        print(head.data)
        head = head.next
    print(f"for test head in func: {head}")

def reverse_linkedList(head):
    """
 (n)   1->2->3->n : n<-1<-2<-3
  ^    ^
prev  curr 
    """
    prev, curr = None, head
    while curr is not None:
        temp = curr.next        
        curr.next = prev  #n<-1<-2 3 n
        prev = curr
        curr = temp
    return prev

def reverse_linkedListRec(head):
    #1->2->3->4->n
    if head is None or head.next is None:
        return head
    
    #(h)1->|2|
    #   n<-|2|<-3<-4(newHead)
    newHead = reverse_linkedListRec(head.next)
    #   1<-|2|<-3<-4

    head.next.next = head # (h)1<-2<-3<-4
    head.next = None #n<-(h)1<-2<-3<-4
    return newHead

if __name__ == '__main__':
    head = insert()
    # print(f"head before: {head}") 
    # print(f"{head.data}->{head.next.data}->{head.next.next.data}->{head.next.next.next}")
    print_list(head)
    head =  reverse_linkedList(head)
    print_list(head)
    # print(f"head after: {head}")
