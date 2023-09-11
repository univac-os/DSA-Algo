class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        #heap based on group size add number 
        minH=[]
        res=[]
        for idx,size in enumerate(groupSizes):
            heapq.heappush(minH,(size,idx)) #(3,0) (3,1),(1,5)..
        
        #now we need to create new list for same group size
        count=0
        while minH:
            size,idx=heapq.heappop(minH)
            if count==0:
                #1st occurance
                res.append([])
                count=size
            res[-1].append(idx)
            count-=1
        
        return res
        
        
        #map of group and number 
        #GREEDY
        groups={}
        res=[]
        for idx,grp in enumerate(groupSizes):
            if grp not in groups:
                groups[grp]=[]
            groups[grp].append(idx)
        
            #make list of group
            if len(groups[grp])==grp:
                #add to res and make new group
                res.append(groups[grp])
                groups[grp]=[]
        
        return res
        