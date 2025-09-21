class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        stack to check char
        """
        st=[] # (char,cont_count)
        for c in s:
            if st and st[-1][0]==c:
                st[-1][1]+=1
                if st[-1][1]==k:
                    st.pop()
            else:
                st.append([c,1])
        res=""
        for char,cnt in st:
            res+=char*cnt
        return res
        