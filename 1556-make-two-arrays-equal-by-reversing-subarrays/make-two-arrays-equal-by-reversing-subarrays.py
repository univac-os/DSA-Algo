class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        #another way is create hashmap add element from targert and delete the element of the arr
        # from hashmap and check finally hashmap is empty O(n) 
        count=defaultdict(int)
        for n1,n2 in zip(target,arr):
            count[n1]+=1
            count[n2]-=1
        for n in count:
            if count[n]!=0:
                return False
        return True
        
        #similar to isAnagram
        return Counter(target)==Counter(arr)