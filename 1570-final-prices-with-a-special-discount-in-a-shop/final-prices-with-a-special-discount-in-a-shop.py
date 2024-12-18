class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # looks like next smallest element NSE
        # use monotonic increasing stack O(N)
        #stack with indexes
        res=prices.copy()
        stack=[]
        for i in range(len(prices)):
            while stack and prices[stack[-1]]>=prices[i]:
                #then we got next previous value
                j=stack.pop()
                res[j]-=prices[i]
            stack.append(i)
        return res