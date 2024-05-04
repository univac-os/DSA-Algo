class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #sort and take value O(nlogn+n)
        #Greedy can we use maxheap --yes but we need smallest value to have pair
        #so sort and 2 ptr
        people.sort()
        l,r=0,len(people)-1
        res=0
        while l<=r:
            remaining=limit-people[r]
            r-=1
            if l<=r and remaining>=people[l]:
                l+=1
            res+=1

        return res
        
        