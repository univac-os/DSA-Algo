class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """
        we want substring 1st half=2nd half so here len is even
        we want to idx map of char and check the index to get the presence
        this does work as if aaaa we will only get 1 a check aa aa is also answer
        so better we need to check substring will be O(n//2 * n//2 * n//2)-->O(n3) here we can optmize the string comparsion using hashing 
        so we precompute hashing at every index and check hash will be O(1) and we get O(n2) 
        """
        n = len(text)
        res = set()
        
        # Step 0: Define base and mod for hashing
        base = 31  # A prime number for hashing
        mod = 10**9 + 1  # A large prime modulus
        
        # Step 1: Precompute prefix hashes and powers
        prefix_hash = [0] * (n + 1)
        power = [1] * (n + 1)
        
        for i in range(n):
            prefix_hash[i + 1] = (prefix_hash[i] * base + (ord(text[i]) - ord('a'))) % mod
            power[i + 1] = (power[i] * base) % mod
        
        # Step 2: Helper function to get the hash of the substring text[l:r]
        def get_hash(l, r):
            return (prefix_hash[r] - prefix_hash[l] * power[r - l]) % mod        
        
        # Step 3: Iterate through all possible substring lengths (even-length substrings)
        for l in range(1, n // 2 + 1):  # Length of the half of the substring
            for i in range(n - 2 * l + 1):  # Ensure we don't exceed the bounds
                # Compare the two halves of the current substring
                hash1 = get_hash(i, i + l)  # First half: text[i:i+l]
                hash2 = get_hash(i + l, i + 2 * l)  # Second half: text[i+l:i+2*l]
                
                # If the hashes match, add the full substring to the result set
                if hash1 == hash2:
                    res.add(text[i:i + 2 * l])
        
        # Return the number of distinct substrings
        return len(res)