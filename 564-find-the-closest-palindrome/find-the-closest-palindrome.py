class Solution:
    def nearestPalindromic(self, p: str) -> str:
        '''
        case 1-> take middle  make pallidrome
        case 2-> take middle-1 make pallindrome (smallest)
        case 3-> take middle+1 make pallindrome (largest)
        EDGE CASE
        n=10000--> 10 0 01 , 109 01  ,10 1 01 , 9999 ,99999 ,1 000 1 
        n=1234 --> 12 21 , 13 31 ,11 11
        we need make all 9 and 1 0*(n-2) 1
        '''
        N = len(p)
        if p=="1":return "0"
        first_half = p[:(N + 1) // 2]
        candidates = set()
        
        # Generate potential palindromes based on the first half
        for d in [-1, 0, 1]:
            first_half_with_d = str(int(first_half) + d)
            if N % 2 == 0:
                candidates.add(first_half_with_d + first_half_with_d[::-1])
            else:
                candidates.add(first_half_with_d + first_half_with_d[-2::-1])
        
        # Handle special cases
        if N-1>0:
            candidates.add("9" * (N - 1))  # For cases like 1000 -> 999
        candidates.add("1" + "0" * (N - 1) + "1")  # For cases like 999 -> 1001
        
        candidates.discard(p)  # Remove the number itself if present in candidates

        # Find the closest palindrome
        closest_palindrome = None
        min_diff = float('inf')
        
        for candidate in candidates:
            diff = abs(int(candidate) - int(p))
            if diff < min_diff or (diff == min_diff and int(candidate) < int(closest_palindrome)):
                min_diff = diff
                closest_palindrome = candidate
        
        return closest_palindrome

