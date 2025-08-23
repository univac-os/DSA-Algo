# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        we can get a head start to ptr and remove the link when we reach
        """
        slow,fast=head,head
        for i in range(n):
            fast=fast.next
        if not fast: #edge case where we want to remove 1st node
            return head.next

        while fast and fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head