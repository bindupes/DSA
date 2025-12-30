# . How do you find the middle element of a singly  linked list ?  

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
    def find_middle_num(head):
        length=0
        current=head
        while current:
            length+=1
            current=current.next
        
        mid=length//2
        current=head
        for _ in range(mid):
            current=current.next
        return current.data
