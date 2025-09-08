class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        convert to str and then add +1 then convert to list
        int(''.join(map(str,digits))) +1 ) join num to str 123 +1 
        str(int(''.join(map(str,digits))) +1 ) convert 124 to str
        map(int,str(124)) to 124 interger and finally list [1,2,4]
        """
        return list(map(int,str(int(''.join(map(str,digits))) +1 )))