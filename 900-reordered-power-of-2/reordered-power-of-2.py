class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        last digit should be 2,4,8,6 but what about the n-1 digit n-2..
        counter of digit need,for remaining we can check 2^31 %number give or not --take time
        above does not work as well say 215 --> 512 12 is not divisible
        so get the count of number and check with power of 2 number
        """
        count=Counter(str(n))
        for i in range(32):
            power_2=1<<i
            count_p=Counter(str(power_2))
            if count==count_p:
                return True
        return False