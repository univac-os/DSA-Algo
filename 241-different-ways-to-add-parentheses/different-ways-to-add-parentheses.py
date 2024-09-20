class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        #recursion backtrack as we want combinations
        #at each operator we will break into 2 O(2^n) and combine of O(n2^n)
        operator={
            "+" : lambda x,y : x+y,
            "-" : lambda x,y : x-y,
            "*" : lambda x,y : x*y
        }

        def backtrack(l,r):
            res=[]
            for i in range(l,r+1):
                op=expression[i]
                if op in operator: #we need to divide
                    nums1=backtrack(l,i-1)
                    nums2=backtrack(i+1,r)

                    for n1 in nums1:
                        for n2 in nums2:
                            #combination
                            res.append(operator[op](n1,n2))
            
            if res==[]:#say we dont have operator 12
                res.append(int(expression[l:r+1]))
            
            return res
        
        return backtrack(0,len(expression)-1)