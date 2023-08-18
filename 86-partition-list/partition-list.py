# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #preserve the order so use 2 linkedlist and connect them 
        left,right=ListNode(),ListNode() #dummy node
        ltail,rtail=left,right #add the node to list
        while head:
            if head.val<x:
                #add to left list
                ltail.next=head
                ltail=ltail.next
            else:
                #add to right list
                rtail.next=head
                rtail=rtail.next
            head=head.next
        
        #connect left end to right start
        ltail.next=right.next
        #make right end as null
        rtail.next=None

        return left.next