class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        #custom sort --check no of occurance and if both are same check which is larger value 
        #to check larger value we use -n and give smallest -ve value 
        count=Counter(nums)

        nums.sort(key=lambda n:(count[n],-n))
        return nums