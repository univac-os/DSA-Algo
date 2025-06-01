from math import comb
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        math combinations 2 2 1 so 3!/2! , 1 1 1 so 3!/3! =1 so 3! is constant
        but problem here  1 2 2 so 3!/2! but both are same so we will count multiple times
        so O(n2) a,b find c and check 
        line of n chocolate draw 2 line (0 also included) we have n+2 option (n+2)C2 =n*
        now restrict such that 1 get alway more that limit (n+2 - limit+1)C 2 so 3 option (a,b,c)
        similar 2 get more that limit (n+2 -2*(limit+1))C 2 (ab,bc,ca)
        similar 3 (n+2 -3*(limit+1)) C 2 (abc)
        """
        def count(n):
            # C(n + 2, 2) — number of non-negative integer solutions for 3 variables
            return comb(n + 2, 2) if n >= 0 else 0

        total = count(n)

        # Inclusion-Exclusion
        total -= 3 * count(n - (limit + 1))               # A, B, C
        total += 3 * count(n - 2 * (limit + 1))           # A∩B, B∩C, C∩A
        total -=     count(n - 3 * (limit + 1))           # A∩B∩C

        return total