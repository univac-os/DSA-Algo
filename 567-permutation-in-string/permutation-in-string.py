class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        sliding window but we need matches
        1. hashmap for s1 and s2 check the count of char in s1 same as s2 in that window O(26n)
        2.Better same hashmap here we will have matches
        """
        if len(s1) > len(s2):
            return False

        

        # Count characters in s1
        s1_count = Counter(s1)
        window_count = Counter()

        # Sliding window over s2
        for i in range(len(s2)):
            # Add the current character to the window
            window_count[s2[i]] += 1

            # Remove the character that is left out of the window
            if i >= len(s1):
                if window_count[s2[i - len(s1)]] == 1:
                    del window_count[s2[i - len(s1)]]
                else:
                    window_count[s2[i - len(s1)]] -= 1

            # Compare the two counters
            if window_count == s1_count:
                return True

        return False