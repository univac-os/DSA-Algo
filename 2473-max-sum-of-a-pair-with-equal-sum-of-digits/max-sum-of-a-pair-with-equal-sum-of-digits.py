class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """
        hashmap of sum and take the value max O(n)+O(k) k=sum of element
        """
        nums.sort()
        count=defaultdict(list)
        for n in nums:
            num=list(map(int,str(n)))
            count[sum(num)].append(n)
        print(count)
        maxi=-1
        for k,v in count.items():
            if len(v)>=2:
                s=v[-1]+v[-2]
                maxi=max(maxi,s)
        return maxi
