class Solution:
    def decodeString(self, s: str) -> str:
        """
        stack O(n)
        """
        st=[]
        for c in s:
            if c==']':
                tmp=[]
                while st and st[-1]!='[' :
                    tmp.append(st.pop())
                st.pop()#removed [ opening
                tmp = tmp[::-1]  # reverse to correct order
                num = []
                while st and st[-1].isdigit():
                    num.append(st.pop())
                num = int("".join(num[::-1])) if num else 1
                st.append(''.join(tmp)*num)
            else:
                st.append(c)
        return ''.join(st)
                
