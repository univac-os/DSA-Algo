class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        """
        O(n*m) take each element and check with other elements and find mini operation
        so sort the values so middle value is answer 
        WHY middle value?--> median of array is middle way is like same distance to travel to left and right
        O(mnlogmn) and space is O(mn)
        """
        nums=[grid[i][j] for j in range(len(grid[0])) for i in range(len(grid))]
        nums.sort()
        #find median before than check whether its possible with every num check by mod
        base=nums[0]%x
        if any(num%x !=base for num in nums):
            return -1
        median=nums[len(nums)//2]
        return sum(abs(num-median)//x for num in nums)