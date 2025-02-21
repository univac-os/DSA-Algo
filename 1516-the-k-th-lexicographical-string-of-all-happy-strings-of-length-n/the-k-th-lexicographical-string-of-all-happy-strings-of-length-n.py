class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        get all combination 3*(2^(n-1)) and sort them in sorted and find kth 
        BETTER ? drawing the tree 
        say n=3  3_ 2_ 2_ 3*2*2 first we have 3 option next 2 ,next 2 ... so total 3*2^(n-1)
        here we have 12 for starting with a we have 4 ,with b 4 ,with c 4 so 12/3
        now if know first letter is say b the next char will be a or c (2 option)
        so first 2 are b a _ and next are b c _
        next we have 2 option b a b /b a c and b c a /b c b 
        so now k=10
        1-4 --> a | 5-8 --> b | 9-12 --> c first letter  here 9<k<12 so first is c
        9.  10 | 11 12
           ca_ |  cb_
        cab cac| cba cbc      O(N)
        """
        total = 3 * (2 ** (n - 1))
        if k > total:
            return ""  # If k is out of range, return an empty string
        res = []
        left, right = 1, total
        choices = ["a", "b", "c"]

        for _ in range(n):
            curr = left
            partition_size = (right - left + 1) // len(choices)
            for ch in choices:
                if curr <= k < curr + partition_size:
                    res.append(ch)
                    left = curr
                    right = curr + partition_size - 1
                    # Remove current choice to ensure no adjacent duplicates
                    choices = [c for c in "abc" if c != ch]
                    break
                curr += partition_size

        return "".join(res)

        def backtrack(ds,ans):
            if len(ds)==n:
                ans.append(ds.copy())
                return
            for ch in ['a','b','c']:
                if len(ds)>0 and ds[-1]==ch:
                    continue
                ds.append(ch)
                backtrack(ds,ans)
                ds.pop()
        
        ans=[]
        ds=[]
        backtrack(ds,ans)
        if len(ans)<k:
            return ""
        ans.sort()
        return "".join(ans[k-1])

