def append(self,new_data):
    new_node=Node(new_data)
    if self.head is None:
        self.head=new_node
        return
    last=self.head
    while(last.next):
        last=last.next

    last.next=new_node