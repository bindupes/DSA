# How do you find the third node from the end in a  singly linked list?
def third_from_end(head):
    if head is None:
        return None
        
    first=head
    second=head
    
    for _ in range(3):
        if first is None:
            return None
        first=first.next
        
    while first:
        first=first.next
        second=second.next
    return second.next
