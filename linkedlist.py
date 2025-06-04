class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
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
ll.display()
