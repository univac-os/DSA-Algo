class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        convert to str and then add +1 then convert to list
        """
        return list(map(int,str(int(''.join(map(str,digits))) +1)))