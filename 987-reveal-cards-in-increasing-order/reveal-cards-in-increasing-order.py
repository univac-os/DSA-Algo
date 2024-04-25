class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        #1.sort -- we need in increasing order
        #2. index how can i get 
        #we are keep in alternative position which runs circular so queue
        #fill even position then fill odd position
        deck.sort()
        q=deque(range(0,len(deck))) # queue with index
        res=[0]*len(deck)

        for n in deck:
            idx=q.popleft()
            res[idx]=n
            #move the next index to back
            if q:
                next_idx=q.popleft()
                q.append(next_idx)
        return res
        