class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        #check difference when to use which one so assume to use bricks completely and use ladder
        maxHeap=[]
        for i in range(len(heights)-1):
            diff=heights[i+1]-heights[i]
            if diff<=0:
                continue
            #we need to use bricks till its exhauted 
            bricks-=diff
            heapq.heappush(maxHeap,-diff) #used bricks
            if bricks<0:
                #now check ladder is better option to use
                if ladders==0:
                    return i # all resource used
                ladders-=1 #use it so check prev place where more bricks are used
                max_bricks_used= -heapq.heappop(maxHeap)
                bricks+=max_bricks_used

        return len(heights)-1 # we are still resource with us
        