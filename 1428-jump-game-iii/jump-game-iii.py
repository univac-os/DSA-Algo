class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        DP at every point 2 option and we need to select anyone and visited to remove cycle
        """
        visit=set()
        def dfs(i):
            if i<0 or i>=len(arr): return False
            if i in visit: return False
            if arr[i]==0: return True
            visit.add(i)
            return dfs(i+arr[i]) or dfs(i-arr[i])

        return dfs(start)