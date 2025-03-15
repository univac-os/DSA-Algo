class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        we will have min heap of len k only ,whenever required we remove low freq value from heap
        BETTER is use bucket sort have counter and an array of freq where we will add num to taht freq num
        """
        count=Counter(nums)
        freq=defaultdict(list)
        for num,cnt in count.items():
            freq[cnt].append(num)
        res=[]
        freq = dict(sorted(freq.items(),reverse=True)) #gives turple by default
        for cnt,lt in freq.items():
            for l in lt:
                if len(res)<k:
                    res.append(l)
        return res
        count=Counter(nums) #num:count
        min_h=[]

        for num,cnt in count.items():
            heapq.heappush(min_h,(cnt,num))#key is cnt
            if len(min_h)>k:
                #pop less 
                heapq.heappop(min_h)
        return [ n for _,n in reversed(min_h)]