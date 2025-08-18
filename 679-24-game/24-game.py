class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        """
        24 = 2*12 | 3*8 | 4*6 but we can have addition all division some real division so we need see combination ,so Backtracking so each number 6 options (a+b ,a*b , a-b ,b-a ,a/b,b/a) and check it so from each option check it so time complexity will be huge 
        """
        approx=1e-6 #10^6
        def dfs(nums):
            if len(nums)==1:
                return abs(nums[0]-24.0)<approx 
            n=len(nums)
            for i in range(n):
                for j in range(i+1,n):
                    a,b=nums[i],nums[j]
                    options ={a+b,a*b,a-b,b-a} #set
                    remain=[nums[k] for k in range(n) if k!=i and k!=j]
                    if b>approx:
                        options.add(a/b)
                    if a>approx:
                        options.add(b/a)
                    
                    for val in options:
                        if dfs(remain + [val]):
                            return True
            return False
        
        return dfs([float(x) for x in cards])