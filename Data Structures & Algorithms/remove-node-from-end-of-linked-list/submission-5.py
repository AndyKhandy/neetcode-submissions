# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        spacing = n - 1
        left, right = head, head

        for i in range(spacing):
            right = right.next
        
        prev = temp = ListNode(0,head)
        
        while right.next:
            prev = left
            left = left.next
            right = right.next

        prev.next = left.next
        
        return temp.next


        
        

        