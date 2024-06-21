class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #greedy but we need window to check so sort wont work
        #sliding window-O(n)
        l=0
        wind,max_wind=0,0
        pakka_cust=0
        for r in range(len(customers)):
            if grumpy[r]:
                wind+=customers[r]#flipping 
            else:
                pakka_cust+=customers[r]
            if r-l+1>minutes:
                #remove if grumpy is 1 
                if grumpy[l]:
                    wind-=customers[l]
                l+=1
            max_wind=max(max_wind,wind)
        return pakka_cust+max_wind
