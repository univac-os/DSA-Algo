from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Uses backtracking with character counts to count unique sequences.
        Passing `res` as a parameter and returning the accumulated count.
        """
        count = Counter(tiles)

        def backtrack(res: int) -> int:
            for c in count:
                if count[c] > 0:
                    count[c] -= 1  # Choose the character
                    res = backtrack(res + 1)  # Recurse with updated count
                    count[c] += 1  # Undo the choice (backtrack)
            return res  # Return the accumulated count

        return backtrack(0)  # Start with res = 0
