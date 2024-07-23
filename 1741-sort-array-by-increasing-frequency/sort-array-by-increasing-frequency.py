class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        #custom sort 
        count=Counter(nums)

        nums.sort(key=lambda n:(count[n],-n))
        return nums