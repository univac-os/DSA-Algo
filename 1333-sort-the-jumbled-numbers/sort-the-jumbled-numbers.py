class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        #convert into with mapping and check value 
        #if same value check index 
        pairs=[]
        for i,n in enumerate(nums):
            n=str(n)
            mapping_n=0
            for c in n:
                mapping_n*=10
                mapping_n+=mapping[int(c)]
            pairs.append((mapping_n,i))

        pairs.sort()
        return [ nums[p[1]] for p in pairs] #index map to nums index

