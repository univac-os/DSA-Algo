class Solution:
    def minimumPushes(self, word: str) -> int:
        #get the count of letter and maxHeap O(1) as 26 letter is constant
        count=Counter(word).values()
        #we got list of all count of letter
        maxH=[-n for n in count]
        heapq.heapify(maxH)
        res=0
        idx=0
        while maxH:
            cnt = -heapq.heappop(maxH)
            res +=cnt *(1+idx//8)
            idx+=1
        return res