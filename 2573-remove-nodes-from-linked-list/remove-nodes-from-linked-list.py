# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #reverse and now check which are less than that and remove them(skip them) 
        # 5->2->13->3->8 ==> 8->3->13->2->5 ==> 8->(3-skip)->13-->(2,5--skip)
        def reverse(head):
            prev,curr=None,head
            while curr:
                nxt=curr.next
                curr.next=prev
                prev,curr=curr,nxt
            return prev

        head=reverse(head) #1st time
        #skip nodes
        curr=head
        curr_max=curr.val
        while curr.next:
            if curr.next.val<curr_max:
                #skip them
                curr.next=curr.next.next
            else:
                #take them
                curr_max=curr.next.val
                curr=curr.next
    
        return reverse(head)
        #monotonic decreasing stack -O(n) space-O(n)
        stack=[]
        curr=head
        while curr:
            while stack and curr.val>stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr=curr.next
        #we need to create linked list from stack
        dummy=ListNode()
        curr=dummy
        for n in stack:
            curr.next=ListNode(n)
            curr=curr.next
        return dummy.next