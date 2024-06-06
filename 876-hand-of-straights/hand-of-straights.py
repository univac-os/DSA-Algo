class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #hashmap to have count of nums
        #we need to take min value at start so min Heap 
        #from here go on and remove if count is 0 --> O(nlogn)
        if len(hand)%groupSize:
            return False
        count=Counter(hand)
        minH=list(count.keys())
        heapq.heapify(minH)#O(n) operation
        while minH:
            first=minH[0]
            for i in range(first,first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    #say 1-->2 2-->0 3-->1 so there is break as 2 is over
                    if i!=minH[0]:
                        return False
                    heapq.heappop(minH)#remove that element
        return True