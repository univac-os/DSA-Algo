class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        """
        IMP 2 basket sorting gives same baskets so we want pair of numbers 
        sort and find the avg(should be int) and based on the find the swapping element greedy but which pair we need to go not proper so have the cout of freq of char helP?
        same number delete from both side ,diff not good with example checked
        """
        basket1.sort()
        basket2.sort()
        freq=Counter()
        mini=float('inf')
        for b1 in basket1:
            freq[b1]+=1
            mini=min(mini,b1)
        for b2 in basket2:
            freq[b2]-=1
            mini=min(mini,b2)
        
        extra=[]
        for fruit,val in freq.items():
            if val%2!=0:
                return -1 #Not possible
            extra.extend([fruit]*(abs(val)//2))
        print(extra)
        if not extra:
            #both are equal
            return 0
        
        extra.sort()
        #swap small and big or swap mini val with element each time so till middle is needed
        return sum(min(2*mini,x) for x in extra[:len(extra)//2])