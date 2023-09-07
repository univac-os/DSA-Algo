# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #3 parts 1.get left 2.reverse till right 3.making the list connection
        dummy=ListNode(0,head) #if left is 1

        #1. get list
        leftPrev,curr=dummy,head 
        for i in range(left-1):
            leftPrev,curr=curr,curr.next
        
        # 2. reverse till right
        prev,nxt=None,curr
        for i in range(right-left+1):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        # 3. connection now curr is outside the region prev is at end
        leftPrev.next.next=curr # 2-->5
        leftPrev.next=prev #1 -->4

        return dummy.next #point to head
        

