class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print('The Given Previous node must be in LinkedList:')
            return

        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
            last.next=new_node

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__=='__main__':
    list1=LinkedList()
    list1.append(6)
    list1.push(7)
    list1.push(1)
    list1.append(4)
    list1.insertAfter(list1.head.next,8)

    print("The Created List is:",list1.printList())
