# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l,r = head,head
        spacing = n - 1

        for i in range(spacing):
            r = r.next

        prev = dummy = ListNode(0,head)

        while r.next:
            prev = l
            l = l.next
            r = r.next

        prev.next = l.next

        return dummy.next



