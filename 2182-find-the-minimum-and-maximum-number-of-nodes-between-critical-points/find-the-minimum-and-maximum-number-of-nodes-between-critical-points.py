# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def critical (self,prev,curr,nxt):
        return (prev.val<curr.val>nxt.val or prev.val>curr.val<nxt.val)
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        #check the local min/max and store them and check them O(N)
        prev,curr,nxt=head,head.next,head.next.next
        first_pt,prev_pt=0,0
        mini,maxi=float('inf'),float('-inf')
        idx=1 #start from 1th index check as extreme points cant be taken
        while nxt:
            if self.critical(prev,curr,nxt):
                #check if we got 1st point or not
                if first_pt:
                    maxi=idx-first_pt
                    mini=min(mini,idx-prev_pt)
                else:
                    #we got first ptr
                    first_pt=idx
                prev_pt=idx
            
            prev,curr,nxt=curr,nxt,nxt.next
            idx+=1

        return [mini,maxi] if mini!=float('inf') else [-1,-1]