class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #pick or not pick. if not picking we need to not take the number value itself not index
        #backtracking -->we need all the combination
        res=[]
        candidates.sort()
        def dfs(i,ds,total):
            if total==0:
                return res.append(ds.copy())
            
            if i+1>len(candidates) or total<0:
                return
            #pick
            ds.append(candidates[i])
            dfs(i+1,ds,total-candidates[i])
            #not pick
            ds.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,ds,total)
        
        dfs(0,[],target)
        return res
