def insertAfter(self,prev_node,new_data):
    if prev_node is None:
        #1.Check If prev node exist
        print("The given previous node must in Linked List")
        return
    #2 Create New Node
    #3 Put in the data
    new_node=Node(new_data)
    #4 make next of new node as prev node
    new_node.next=prev_node.next
    #5 make next of prev node as new node
    prev_node.next=new_node

