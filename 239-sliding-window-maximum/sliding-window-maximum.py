from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #use deque in decreasing order as we want maximum in that window
        dec=deque()# add index as we need to check size of window
        res=[]
        for idx in range(len(nums)):
            #remove if its not the current window
            while dec and dec[0]==idx-k :
                dec.popleft()# remove them
            
            #make sure deque in decreasing order
            while dec and nums[dec[-1]]<=nums[idx]: # 5 3 6 check 6,3 remove 3,check 5 6 remove 5 
                dec.pop()#pop right

            dec.append(idx)

            # add to res 
            if idx>=k-1 :
                res.append(nums[dec[0]])

        return res