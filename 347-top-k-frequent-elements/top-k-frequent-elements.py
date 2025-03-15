class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        we will have min heap of len k only ,whenever required we remove low freq value from heap
        """
        count=Counter(nums) #num:count
        min_h=[]

        for num,cnt in count.items():
            heapq.heappush(min_h,(cnt,num))#key is cnt
            if len(min_h)>k:
                #pop less 
                heapq.heappop(min_h)
        return [ n for _,n in reversed(min_h)]