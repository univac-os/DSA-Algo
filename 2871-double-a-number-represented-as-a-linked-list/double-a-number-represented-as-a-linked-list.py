# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #traverse store the value and update the values -O(n) space-O(1)
        #stack O(n)
        #reverse LL O(n) muliple each one and reverse them O(n)
        #2 ptr prev and curr check carry if there is carry then update prev val O(n)
        curr=head
        prev=None
        while curr:
            twice=curr.val*2
            if twice <10:
                curr.val=twice
            elif prev:
                #update carry
                curr.val=twice%10
                prev.val+=1
            else:
                #create prev val occurs at start only
                head=ListNode(1,curr)
                curr.val=twice%10
            prev=curr
            curr=curr.next
        return head
        
        