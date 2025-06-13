class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("emty linked list")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next
    def delete_begining(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
    def delete_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is  not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
    def delete_position(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            prev = prev.next
            temp = temp.next
        prev.next = temp.next
L = SLL()
n1 = Node(10)
L.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
n5 = Node(50)
n4.next = n5
L.delete_begining()
L.delete_end()
L.delete_position(2)
L.display()

