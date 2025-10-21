class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """
        we want fill lake and 0 value so we want to dry a lake if we find that lake 
        so here number are the lake number where rains falls
        1 2 2 1 so rain falls on 1 then 2 and again 2 and 1 -so here if have 0 first dry 2 as it comes first then 1
        """
        n=len(rains)
        res=[1]*n
        st=SortedList() # drying area in increasing order based on index
        mp={} #lake-num-->index
        for idx,r in enumerate(rains):
            if r==0:
                st.add(idx)
            else:
                res[idx]=-1
                #first time no problem if not then use drying area
                if r in mp:
                    dry_day=st.bisect(mp[r])
                    if dry_day==len(st):
                        #no found so flood
                        return []
                    res[st[dry_day]]=r
                    st.discard(st[dry_day])
                mp[r]=idx
        return res