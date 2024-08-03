class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        #similar to isAnagram
        return Counter(target)==Counter(arr)