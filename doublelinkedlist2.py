class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev  = None
class DLL:
    def __init__(self):
        self.head = None
    def insert_begining(self,data):
        n = Node(data)
        temp = self.head
        temp.prev = n
        n.next = temp
        self.head = n
    def insert_end(self,data):
        n = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = n
        temp.prev = temp
    def insert_position(self,pos,data):
        n = Node(data)
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        n.prev = temp
        n.next = temp.next
        temp.next.prev = n
        temp.next = n
    def delete_begining(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None
    def delete_end(self):
        temp = self.head.next
        before = self.head
        while temp.next is not None:
            temp = temp.next
            before = before.next
        before.next = None
        temp.prev = None
    def delete_pos(self,pos):
        temp = self.head.next
        before = self.head
        for i in range(1,pos-1):
            temp = temp.next
            before = before.next
        before.next = temp.next
        temp.next.prev = before
        temp.prev =None
        temp.next = None

    def display(self):
        if self.head is None:
            print("empty DLL ")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end = " ")
                temp = temp.next

L = DLL()
n1 = Node(10)
L.head = n1
n2 = Node(20)
n1.next = n2
n2.prev = n1
L.insert_begining(5)
L.insert_end(30)
L.insert_position(4,25)
L.delete_begining()
L.delete_end()
L.delete_pos(2)
L.display()
