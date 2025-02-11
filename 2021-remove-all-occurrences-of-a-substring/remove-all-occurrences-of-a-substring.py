class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        sliding window as we want continuous string but we found match we want to remove them on fly so better use stack
        """
        def match():
            #we want from stack last element till len of path
            want=stack[-len(part):]
            return "".join(want)==part

        stack=[]
        for i in range(len(s)):
            stack.append(s[i])
            #check match or not
            if len(stack)>=len(part) and match():
                for _ in range(len(part)):
                    stack.pop()
                    
        return "".join(stack)