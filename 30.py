'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
 '''

class ListNode(object): # to create one node
    def __init__(self ,val=0,next=None):
        self.val = val
        self.next=next

    def create_linked_list(nums):#to create a linked list
        dummy=ListNode(0)
        current=dummy
        for num in nums:
            current.next=ListNode(num)
            current=current.next
        return dummy.next

class Solution(object):
    def addTwoNumbers(self,l1,l2):
        dummy=ListNode(0)
        current=dummy
        carry=0

        while l1 or l2:
            val1= l1.val if l1 else 0
            val2= l2.val if l2 else 0

            total = val1+val2 +carry
            carry= total//10

            current.next = ListNode(total%10)
            current=current.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry>0:
            current.next=ListNode(carry)
            
        return dummy.next
    
def print_linked_list(node):   # to convert linked list into list , to print values in list 
    result=[]
    while node:
        result.append(node.val)
        node=node.next
    print(result)


sol = Solution()
l1= ListNode.create_linked_list([2,4,3])
l2=ListNode.create_linked_list([5,6,4])
result=sol.addTwoNumbers(l1,l2)
print_linked_list(result)