class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        mono increasing stack find the len of stack then is answer at each point and remove to maintain the order
        """
        st,res=[],[]
        for h in reversed(heights):
            cnt=0
            while st and st[-1]<h:
                st.pop()
                cnt+=1 #smaller to it
            if st:
                #bigger to it
                cnt+=1
            res.append(cnt)
            st.append(h)
        return res[::-1]