class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #O(n2)-nested loop
        #O(n) using hashset O(n)-space
        #O(n) without space use condition [1,n] so visit the index and mark them
        #HOW TO MARK? --make number -ve
        res=[]
        for n in nums:
            n=abs(n)
            if nums[n-1]<0:
                res.append(n)
            nums[n-1]=-nums[n-1]
        return res

        