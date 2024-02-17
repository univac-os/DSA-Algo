class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #conditon1-- so sort
        #condition2-- take sum and check GREEDY
        nums.sort()
        res=-1
        total=0
        for n in nums:
            if total>n:
                res=total+n #2nd condition
            total+=n
        return res