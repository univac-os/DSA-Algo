class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_queue,neg_queue=deque(),deque()
        for n in nums:
            if n>0:
                pos_queue.append(n)
            else:
                neg_queue.append(n)
        i=0
        while 2*i <len(nums):
            #1st + 2nd -
            nums[2*i]=pos_queue.popleft()
            nums[2*i+1]=neg_queue.popleft()
            i+=1
        return nums
        