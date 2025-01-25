class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        """
        greedy wont work limit=1 [3,2,1]--> [2,3,1]
        so we need form group which has in limit and use them 
        sort the number then find the group and pop each one O(nlogn + n + n)
        """
        groups=[]#list of queue as we need take 1st element 
        g_map={} # num[i] -> g_index
        #since we sorted so value is group are increasing order
        for n in sorted(nums):
            #create new group if exceeds limit
            if not groups or abs(n- groups[-1][-1])>limit:
                groups.append(deque())

            groups[-1].append(n)
            g_map[n]=len(groups)-1

        res=[]
        for n in nums:
            g_idx=g_map[n]
            res.append(groups[g_idx].popleft())#take the element from that group based on g_index
        return res