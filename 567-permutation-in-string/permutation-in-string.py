class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        sliding window but we need matches
        1. hashmap for s1 and s2 check the count of char in s1 same as s2 in that window O(26n)
        2.Better use array of 26 and check the value
        """
        if len(s1) > len(s2):
            return False

        s1_count=[0]*26
        window_count=[0]*26

        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')]+=1

        for i in range(len(s2)):
            window_count[ord(s2[i])-ord('a')]+=1

            if i >=len(s1):
                #Move window
                window_count[ord(s2[i -len(s1)])-ord('a')]-=1
            if window_count==s1_count:
                return True
        return False

        s1_count = Counter(s1)
        window_count = Counter()

        for i in range(len(s2)):
            window_count[s2[i]] += 1
            # Remove the character that is left out of the window
            if i >= len(s1):
                if window_count[s2[i - len(s1)]] == 1:
                    del window_count[s2[i - len(s1)]]
                else:
                    window_count[s2[i - len(s1)]] -= 1

            if window_count == s1_count:
                return True

        return False