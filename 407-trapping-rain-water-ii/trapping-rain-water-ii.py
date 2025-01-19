class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        writing numbers in 2D grid i can see we need to check for each number 4 direction 
        but we want to conitnous boxes count ? HOW
        we will go from border and BFS and find cells which are less than this and add them
        we will use min heap to check from small to larges O(NMlog(mn))
        WHY ITS WORKS we want wall which are bigger so find them and use them to get the result
        https://leetcode.com/problems/trapping-rain-water-ii/solutions/1138028/python3-visualization-bfs-solution-with-explanation
        """
        row,col=len(heightMap),len(heightMap[0])
        min_h=[] # (value,r,c)
        for i in range(row):
            for j in range(col):
                if i in [0,row-1] or j in [0,col-1]:
                    heapq.heappush(min_h,(heightMap[i][j],i,j))
                    heightMap[i][j]=-1 #making it as visited
        
        res=0
        max_h=-1
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        while min_h:
            h,r,c=heapq.heappop(min_h)
            max_h=max(max_h,h)#get max h till that cell
            res+=max_h - h #store water

            for dr,dc in dir:
                nr,nc=r+dr,c+dc
                if 0<=nr<row and 0<=nc<col and heightMap[nr][nc]!=-1:
                    heapq.heappush(min_h,(heightMap[nr][nc],nr,nc))
                    heightMap[nr][nc]=-1#visited

        return res 

            