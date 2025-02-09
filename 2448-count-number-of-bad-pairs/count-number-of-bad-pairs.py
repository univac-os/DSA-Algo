class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        find each pair O(n2) 
        from total pair - good pair
        how to find good pair 
        j-i=nums[j]-nums[i]--> nums[i]-i=nums[j]-j so its like slope
        if 2 points on same pair then good pair
        total pair =nC2=n*(n-1)//2 OR add all indexes
        """
        total=0
        good_pair=defaultdict(int)
        good=0
        for i in range(len(nums)):
            total+=i
            good+=good_pair[nums[i]-i] #check same diff is present
            good_pair[nums[i]-i]+=1
        return total-good