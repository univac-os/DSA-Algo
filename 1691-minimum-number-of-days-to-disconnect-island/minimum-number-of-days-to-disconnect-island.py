class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        #answer can be 0 ,1, 2 we dont need to remove more than 2
        #why we will remove 2 diagonal,by this we are making sure 2 side are surrond by water
        row,col=len(grid),len(grid[0])
        def dfs(r,c,visit):
            if (r<0 or r>=row or c<0 or c>=col or grid[r][c]==0 or (r,c) in visit):
                return 
            visit.add((r,c))
            nei=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for nr,nc in nei:
                if (nr,nc) not in visit:
                    dfs(nr,nc,visit)

        def count_island():
            visit=set()
            count=0
            for r in range(row):
                for c in range(col):
                    if grid[r][c] and (r,c) not in visit:
                        dfs(r,c,visit)
                        count+=1 #we got island chain
            return count
            
        if count_island()==0 or count_island()>1:
            return 0 
        
        #now we got a big island present we need to break so check each land by making it water
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    continue
                #make land to water
                grid[r][c]=0
                #count the island
                if count_island()!=1: #we have split it
                    return 1
                # go and check other land
                grid[r][c]=1
        
        return 2 #if not 0 ,1 then 2 is answer