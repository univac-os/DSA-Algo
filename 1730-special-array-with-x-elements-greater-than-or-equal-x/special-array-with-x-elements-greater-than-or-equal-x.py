class Solution:
    def specialArray(self, nums: List[int]) -> int:
        #sort numbers-O(nlogn) but can we better counting sort
        #check 1 to len(nums)
        #go reverse way
        #get the number greater than the element at that index 
        #find number which match this prefix sum
        count=[0]*(len(nums)+1)
        for n in nums:
            idx=n if n<len(nums) else len(nums)
            count[idx]+=1
        total_right=0
        for i in range(len(nums),0,-1):#[n-->1]
            total_right+=count[i]
            if i==total_right:
                return total_right
        return -1
        