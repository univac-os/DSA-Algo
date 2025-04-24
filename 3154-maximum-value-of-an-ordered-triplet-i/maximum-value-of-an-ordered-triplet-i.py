class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        you should not sort the value looking at example [1,2,3]
        so we want i--> maxi j-->mini k-->maxi
        instead of O(n3)we can go through nums and if we find any max value till now we go and find j and k 
        """
        max_i_minus_j = float('-inf')
        result = 0
        max_i = nums[0]

        for j in range(1, len(nums) - 1):
            max_i_minus_j = max(max_i_minus_j, max_i - nums[j])
            max_i = max(max_i, nums[j])
            result = max(result, max_i_minus_j * nums[j + 1])

        return result


