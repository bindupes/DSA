class Node:
    class __init__(slef,data):
        self.data=data
        self.next=None
        
    class remove_duplicates(head):
        seen=set()
        current=head
        prev=None
        
        while current:
            if current.data in seen:
                perv.next=current.next
            else:
                seen.add(current.data)
                prev=current
            current=current.next
        return head
