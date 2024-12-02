class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #here we need to use prevous smallest element and next smallest element
        #based on this ,we are getting area account each value 
        # arr[i]* (nse-pse -1)
        #here we will compute pse and on going we will find nse for ith val and find area
        n=len(heights)
        stack=[] #(idx)
        res=0
        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]]>=heights[i]):
                #we found nse value for top element in stack
                ith_value=heights[stack[-1]]
                stack.pop()
                if stack:
                    #now after removing top element in pse for ith
                    wd=i-stack[-1]-1 
                else:
                    wd=i #from start we need to consider
                res=max(res,ith_value*wd)
            stack.append(i)
        return res
