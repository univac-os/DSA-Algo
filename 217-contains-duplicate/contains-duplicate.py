class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        have a count array and update this array if we find the value is present then found duplicate
        """
        count=set()
        for n in nums:
            if n in count:
                return True
            else:
                count.add(n)
        return False