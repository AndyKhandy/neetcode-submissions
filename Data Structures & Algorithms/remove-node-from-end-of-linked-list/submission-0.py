# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        spacing = n - 1
        slow,fast = head, head

        for i in range(spacing):
            fast = fast.next

        prev = None
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next

        if(prev):
             prev.next = slow.next
        else:
            return head.next
        

        return head
        