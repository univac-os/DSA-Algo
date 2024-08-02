class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        total_ones=nums.count(1)
        l=0
        wind=max_wind=0
        for r in range(2*n):#circular
            if nums[r%n]:
                wind+=1
            #in circular we might count more ones
            if r-l+1>total_ones:
                wind-=nums[l%n]
                l+=1
            max_wind=max(max_wind,wind)
        return total_ones-max_wind
