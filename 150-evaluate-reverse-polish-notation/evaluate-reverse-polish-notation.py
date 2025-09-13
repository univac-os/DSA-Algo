class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        stack 
        """
        st=[]
        for t in tokens:
            if t.lstrip('-').isdigit():
                st.append(int(t))
            else:
                a=st.pop()
                b=st.pop()
                if t=="+":
                    st.append(b+a)
                elif t=='-':
                    st.append(b-a)
                elif t=='*':
                    st.append(b*a)
                else:
                    st.append(int(b/a))
        return st[0]

                
