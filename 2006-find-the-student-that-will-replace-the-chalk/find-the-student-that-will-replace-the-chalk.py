class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        #simple mod 
        total=sum(chalk)
        mod=k%total
        for i,n in enumerate(chalk):
            if mod >=n:
                mod -=n
            else:
                return i
        return 0

        