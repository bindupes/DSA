# How do you find the middle element of a singly  linked list in one pass?  
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
    def find_middle_num(head):
        slow=head
        fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
