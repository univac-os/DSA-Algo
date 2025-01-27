class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        recursion ? its like combination abc def --> 3*3 = 9 combo
        base case 2 digit so len should be 2
        """
        res=[]
        if digits=="":
            return res

        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(i,ds):
            if i==len(digits):
                res.append("".join(ds))
                return
            
            for letter in phone[digits[i]]:
                ds.append(letter)
                backtrack(i+1,ds)
                ds.pop()

        backtrack(0,[])
        return res