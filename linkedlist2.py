class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None

        
    def insert_begining(self,data):
        nb =Node(data)
        nb.next = self.head
        self.head = nb
    def insert_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
    def insert_position(self,pos,data):
        np = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np
        
    def display(self):
        if self.head is None:
            print("the list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end =" ")
                temp = temp.next


ll = SingleLinkedList()
n =Node(10)
ll.head = n
n1 = Node(20)
n.next = n1
ll.insert_begining(5)
ll.insert_end(25)
ll.insert_position(2,15)
ll.display()
