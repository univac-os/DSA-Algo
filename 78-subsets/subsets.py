class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #we want subset array not how many can be formed
        #if we want count then recursion
        #we want list for backtrack
        res=[]
        ds=[]#subset
        def dfs(i):
            if i==len(nums):
                res.append(ds.copy())
                return
            #include
            ds.append(nums[i])
            dfs(i+1)
            #exclude
            ds.pop()
            dfs(i+1)

        dfs(0)
        return res
        