class Solution:
    def trap(self, height:List[int])->int:
        """
            1.prefix_max start from front and suffix_max from back then 
                min(prefix_max[i]-suffix_max[i])-arr[i] --> O(n) and space O(n)
            2. find leftmax and rightmax 2ptr aproach --> O(n) and space O(1)
            3.llooking at this pattern at any index we want the wall on both side ,
            then calculate the area similar to max area in histogram
            from that index go till you find next greater element,after finding it we will go back and   
            find the area -->O(n) and space O(n)
        """
        n=len(height)
        if n==0:return 0
        stack=[] #(idx)
        res=0
        
        for i in range(n):
            while stack and height[i]>height[stack[-1]]:
                #we found next greater element
                right_wall=stack.pop()
                if not stack:
                    break # no left wall
                distance=i-stack[-1]-1
                ht=min(height[i],height[stack[-1]])-height[right_wall]
                res+=distance*ht
            

            stack.append(i)
        return res

