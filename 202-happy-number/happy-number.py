class Solution:
    def isHappy(self, n: int) -> bool:
        """
        need to store and check it space is there
        """
        store=set()
        while n!=1:
            n=sum([int(i)**2 for i in str(n)])
            if n in store:
                return False
            store.add(n)
        return True