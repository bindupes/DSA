class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
    def length_linked_list(head):
        length=0
        current=head
        
        while current:
            length+=1
            current=current.next
        return length 
        
        
