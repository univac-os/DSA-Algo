class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """
        we want fill lake and 0 value so we want to dry a lake if we find that lake 
        so here number are the lake number where rains falls
        1 2 2 1 so rain falls on 1 then 2 and again 2 and 1 -so here if have 0 first dry 2 as it comes first then 1
        """
        n=len(rains)
        st=SortedList() # zero-index in order based of index
        mp={} # lake-num--index
        res=[1]*n
        for i,r in enumerate(rains):
            if r ==0:
                #add to zero-index
                st.add(i)
            else:
                #check this lake need to be dry before come here
                res[i]=-1
                if r in mp:
                    #check whether the lake from prev --x--current has any 0 in between
                    zero_between=st.bisect(mp[r])
                    if zero_between==len(st):
                        #not present so flood
                        return []
                    res[st[zero_between]]=r #dry that lake
                    st.discard(st[zero_between])#remove from list
                
                mp[r]=i #add current day 
        return res
