class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #O(n2) check each one 
        # hash map --O(n)
        map=defaultdict(int)
        for n in arr:
            map[n]+=1
        
        for n in arr:
            if n !=0 and 2*n in map:
                return True
            if n==0 and map[n]>1:
                return True
        return False
            