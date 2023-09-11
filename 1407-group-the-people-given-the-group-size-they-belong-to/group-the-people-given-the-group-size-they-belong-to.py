class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
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
        