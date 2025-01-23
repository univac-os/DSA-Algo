class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        nodes should be same row or col
        precompute the postion of server based on row and col position and use this
        if we find more than 1 in any position then we comunicate
        precompute O(nm)
        checking is O(k) 
        O(nm + k)
        """
        row_pos=[0]*len(grid)
        col_pos=[0]*len(grid[0])
        position=set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    row_pos[r]+=1
                    col_pos[c]+=1
                    position.add((r,c))
        
        #check row and col position array 
        res=0
        for r,c in position:
            if row_pos[r]>1 or col_pos[c]>1:
                res+=1
        return res
        